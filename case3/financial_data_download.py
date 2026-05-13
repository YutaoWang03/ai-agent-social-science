#!/usr/bin/env python3
"""
financial_data_download.py
==========================
从中证500成分股中筛选300家公司，下载2010-2024年度财务数据，
整理为公司-年份面板格式，输出 financial_panel.csv。

数据来源：AKShare（免费开源，基于新浪财经/东方财富）
使用前需安装：pip install akshare pandas
"""

import os
import sys
import time
import warnings
import datetime
import pandas as pd
import numpy as np

warnings.filterwarnings("ignore")

# ============================================================
# 配置参数
# ============================================================
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
COMPANY_LIST_FILE = os.path.join(OUTPUT_DIR, "company_list.csv")
PANEL_FILE = os.path.join(OUTPUT_DIR, "financial_panel.csv")
START_YEAR = 2010
END_YEAR = 2024
NUM_COMPANIES = 10
SLEEP_SECONDS = 0.5  # 请求间隔，避免被封


def get_csi500_components():
    """获取中证500成分股列表"""
    import akshare as ak
    print("正在获取中证500成分股列表...")
    df = ak.index_stock_cons(symbol="000905")
    df = df.rename(columns={"品种代码": "stock_code", "品种名称": "stock_name", "纳入日期": "in_date"})
    print(f"  获取到 {len(df)} 只成分股")
    return df


def select_companies(components_df, n=300, seed=42):
    """从成分股中选取 n 家公司（优先选纳入日期较早的，确保有足够长的历史数据）"""
    df = components_df.copy()
    df["in_date"] = pd.to_datetime(df["in_date"])
    df = df.sort_values("in_date", ascending=True)
    selected = df.head(n).reset_index(drop=True)
    selected["seq_id"] = range(1, n + 1)
    print(f"  已选取前 {n} 家纳入日期最早的公司")
    return selected


def stock_code_to_sina(code):
    """将6位股票代码转换为新浪财经格式（sh/sz前缀）"""
    code = str(code).zfill(6)
    if code.startswith(("6", "9")):
        return f"sh{code}"
    else:
        return f"sz{code}"


def download_financial_data_single(stock_code_6):
    """
    下载单家公司的利润表和资产负债表年度数据。
    返回整理后的 DataFrame，包含公司代码和年份。
    """
    import akshare as ak

    sina_code = stock_code_to_sina(stock_code_6)

    # ---- 利润表 ----
    try:
        profit_df = ak.stock_financial_report_sina(stock=sina_code, symbol="利润表")
        time.sleep(SLEEP_SECONDS)
    except Exception as e:
        print(f"    [警告] {stock_code_6} 利润表下载失败: {e}")
        return None

    # ---- 资产负债表 ----
    try:
        balance_df = ak.stock_financial_report_sina(stock=sina_code, symbol="资产负债表")
        time.sleep(SLEEP_SECONDS)
    except Exception as e:
        print(f"    [警告] {stock_code_6} 资产负债表下载失败: {e}")
        return None

    if profit_df is None or balance_df is None:
        return None

    # ---- 提取年度报告（12月31日） ----
    def extract_annual(df):
        df = df.copy()
        df["报告日"] = df["报告日"].astype(str)
        # 只保留年报（12月31日）
        df = df[df["报告日"].str.endswith("1231")].copy()
        df["year"] = df["报告日"].str[:4].astype(int)
        df = df[df["year"].between(START_YEAR, END_YEAR)]
        # 只保留合并报表（如有"类型"列）
        if "类型" in df.columns:
            df = df[df["类型"].str.contains("合并", na=False)]
        return df.drop_duplicates(subset=["year"], keep="last")

    profit_annual = extract_annual(profit_df)
    balance_annual = extract_annual(balance_df)

    if profit_annual.empty or balance_annual.empty:
        return None

    # ---- 从利润表提取变量 ----
    profit_cols = {
        "营业收入": "revenue",
        "营业总成本": "total_cost",
        "营业成本": "operating_cost",
        "净利润": "net_profit",
        "营业利润": "operating_profit",
    }
    profit_sub = profit_annual[["year"]].copy()
    for cn, en in profit_cols.items():
        if cn in profit_annual.columns:
            profit_sub[en] = pd.to_numeric(profit_annual[cn], errors="coerce")
        else:
            profit_sub[en] = np.nan

    # ---- 从资产负债表提取变量 ----
    balance_cols = {
        "资产总计": "total_assets",
        "负债合计": "total_liabilities",
        "所有者权益(或股东权益)合计": "total_equity",
        "货币资金": "cash_holdings",
        "流动资产合计": "current_assets",
        "流动负债合计": "current_liabilities",
        "固定资产净额": "fixed_assets",
    }
    balance_sub = balance_annual[["year"]].copy()
    for cn, en in balance_cols.items():
        if cn in balance_annual.columns:
            balance_sub[en] = pd.to_numeric(balance_annual[cn], errors="coerce")
        else:
            balance_sub[en] = np.nan

    # ---- 合并 ----
    merged = pd.merge(profit_sub, balance_sub, on="year", how="outer")
    merged["stock_code"] = str(stock_code_6).zfill(6)

    return merged


def construct_financial_indicators(panel_df):
    """
    构造盈利能力指标和财务控制变量。
    """
    df = panel_df.copy()

    # --- 盈利能力指标 ---
    # ROA = 净利润 / 总资产
    df["ROA"] = df["net_profit"] / df["total_assets"]

    # ROE = 净利润 / 所有者权益
    df["ROE"] = df["net_profit"] / df["total_equity"]

    # 利润率 = 净利润 / 营业收入
    df["profit_margin"] = df["net_profit"] / df["revenue"]

    # 营业利润率 = 营业利润 / 营业收入
    df["operating_profit_margin"] = df["operating_profit"] / df["revenue"]

    # --- 财务控制变量 ---
    # 资产负债率 = 总负债 / 总资产
    df["leverage"] = df["total_liabilities"] / df["total_assets"]

    # 现金持有比例 = 货币资金 / 总资产
    df["cash_ratio"] = df["cash_holdings"] / df["total_assets"]

    # 资本支出代理：固定资产 / 总资产（注意：这是存量指标，非流量）
    df["capex_ratio"] = df["fixed_assets"] / df["total_assets"]

    # 流动比率 = 流动资产 / 流动负债
    df["current_ratio"] = df["current_assets"] / df["current_liabilities"]

    # 企业规模 = ln(总资产)
    df["firm_size"] = np.log(df["total_assets"].abs())

    # 营收增长率（需要按公司排序后计算）
    df = df.sort_values(["stock_code", "year"])
    df["revenue_growth"] = df.groupby("stock_code")["revenue"].pct_change()

    return df


def main():
    print("=" * 60)
    print("上市公司财务数据下载程序")
    print(f"数据范围: {START_YEAR}-{END_YEAR}")
    print("=" * 60)

    # Step 1: 获取中证500成分股
    components = get_csi500_components()

    # Step 2: 选取300家公司
    selected = select_companies(components, n=NUM_COMPANIES)
    selected[["seq_id", "stock_code", "stock_name", "in_date"]].to_csv(
        COMPANY_LIST_FILE, index=False, encoding="utf-8-sig"
    )
    print(f"  公司列表已保存至: {COMPANY_LIST_FILE}")

    # Step 3: 逐公司下载财务数据
    all_data = []
    success_count = 0
    fail_count = 0

    codes = selected["stock_code"].tolist()
    names = selected["stock_name"].tolist()

    print(f"\n开始下载 {len(codes)} 家公司的财务数据...")
    print(f"（每家公司间隔 {SLEEP_SECONDS} 秒，预计总耗时约 {len(codes) * 2 * SLEEP_SECONDS / 60:.0f} 分钟）")

    for i, (code, name) in enumerate(zip(codes, names)):
        pct = (i + 1) / len(codes) * 100
        print(f"  [{i+1}/{len(codes)}] ({pct:.0f}%) {code} {name}...", end=" ", flush=True)

        data = download_financial_data_single(code)
        if data is not None and not data.empty:
            data["stock_name"] = name
            all_data.append(data)
            n_years = data["year"].nunique()
            print(f"✓ ({n_years}年)")
            success_count += 1
        else:
            print("✗ (无数据)")
            fail_count += 1

    print(f"\n下载完成: 成功 {success_count}, 失败 {fail_count}")

    if not all_data:
        print("[错误] 未获取到任何数据，程序退出。")
        sys.exit(1)

    # Step 4: 合并为面板
    panel = pd.concat(all_data, ignore_index=True)
    print(f"\n合并后原始记录数: {len(panel)}")

    # Step 5: 构造指标
    panel = construct_financial_indicators(panel)

    # Step 6: 统一变量名和格式
    # 排序
    panel = panel.sort_values(["stock_code", "year"]).reset_index(drop=True)

    # 选择输出列
    output_cols = [
        "stock_code", "stock_name", "year",
        # 原始变量
        "revenue", "net_profit", "operating_profit", "total_cost", "operating_cost",
        "total_assets", "total_liabilities", "total_equity",
        "cash_holdings", "fixed_assets", "current_assets", "current_liabilities",
        # 构造指标
        "ROA", "ROE", "profit_margin", "operating_profit_margin",
        "leverage", "cash_ratio", "capex_ratio", "current_ratio",
        "firm_size", "revenue_growth",
    ]
    panel = panel[[c for c in output_cols if c in panel.columns]]

    # Step 7: 保存
    panel.to_csv(PANEL_FILE, index=False, encoding="utf-8-sig")
    print(f"面板数据已保存至: {PANEL_FILE}")
    print(f"最终记录数: {len(panel)}")
    print(f"公司数: {panel['stock_code'].nunique()}")
    print(f"年份范围: {panel['year'].min()} - {panel['year'].max()}")

    # 基本统计
    print("\n关键变量描述性统计:")
    desc_cols = ["ROA", "ROE", "profit_margin", "leverage", "cash_ratio", "firm_size"]
    print(panel[desc_cols].describe().round(4).to_string())

    print("\n✓ 全部任务完成！")
    return panel


if __name__ == "__main__":
    main()
