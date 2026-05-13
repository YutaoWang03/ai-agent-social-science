#!/usr/bin/env python3
"""
esg_analysis.py
===============
基于A股上市公司年报文本构造ESG评分面板。

数据来源：巨潮资讯网（cninfo.com.cn）
方法：文本分析 + 关键词匹配 + ESG评分规则

使用前需安装：
pip install requests pdfplumber pandas numpy
"""

import os
import sys
import time
import re
import warnings
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional

warnings.filterwarnings("ignore")

# ============================================================
# 配置参数
# ============================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "data")
COMPANY_LIST_FILE = os.path.join(SCRIPT_DIR, "..", "..", "case3", "data", "company_list.csv")
ESG_PANEL_FILE = os.path.join(OUTPUT_DIR, "esg_panel.csv")
EVIDENCE_LOG_FILE = os.path.join(OUTPUT_DIR, "evidence_log.md")
CODEBOOK_FILE = os.path.join(SCRIPT_DIR, "..", "documents", "codebook.md")
PDF_CACHE_DIR = os.path.join(OUTPUT_DIR, "pdf_cache")

START_YEAR = 2023
END_YEAR = 2023
SLEEP_SECONDS = 1  # 请求间隔


# ============================================================
# ESG关键词词典
# ============================================================
ESG_KEYWORDS = {
    "E": {
        "环境管理": ["环境管理体系", "ISO14001", "环保制度", "环境管理"],
        "污染防治": ["污染物排放", "废水处理", "废气处理", "固废处理", "污染防治", "减排"],
        "资源利用": ["节能减排", "能源消耗", "水资源", "循环利用", "绿色生产", "清洁生产"],
        "环保投入": ["环保投入", "环保支出", "环保投资", "环保费用"],
        "气候变化": ["碳排放", "碳中和", "温室气体", "气候风险", "低碳"],
        "生态保护": ["生态修复", "生物多样性", "生态保护", "绿化"]
    },
    "S": {
        "员工权益": ["员工培训", "职业发展", "薪酬福利", "劳动保护", "员工权益"],
        "职业健康": ["安全生产", "职业健康", "工伤", "安全培训", "职业病"],
        "社区参与": ["社区发展", "公益捐赠", "精准扶贫", "乡村振兴", "社会公益"],
        "供应链管理": ["供应商管理", "供应链责任", "供应商审核"],
        "产品责任": ["产品质量", "产品安全", "客户满意度", "售后服务"],
        "人权保护": ["反歧视", "平等就业", "残疾人就业", "女职工权益"]
    },
    "G": {
        "公司治理": ["董事会", "独立董事", "监事会", "股东大会", "公司治理"],
        "信息披露": ["信息披露", "内幕信息", "关联交易", "定期报告"],
        "合规经营": ["合规管理", "反腐败", "反商业贿赂", "合规经营"],
        "风险管理": ["内部控制", "风险控制", "风险管理", "审计委员会"],
        "股东权益": ["股东回报", "分红", "股利政策", "中小投资者保护"],
        "商业道德": ["商业道德", "廉洁从业", "道德准则"]
    }
}


def load_company_list() -> pd.DataFrame:
    """加载公司列表"""
    df = pd.read_csv(COMPANY_LIST_FILE, encoding='utf-8-sig')
    print(f"加载公司列表: {len(df)} 家公司")
    return df


def fetch_annual_report_urls(stock_code: str, start_year: int, end_year: int) -> Dict[int, str]:
    """
    从巨潮资讯网获取年报PDF链接。
    返回 {年份: PDF_URL} 字典。
    """
    import requests

    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'

    # 判断交易所
    if stock_code.startswith(('6', '9')):
        column = 'sse'
        stock_param = f'{stock_code},gssh0{stock_code}'
    else:
        stock_param = f'{stock_code},gssz0{stock_code}'
        column = 'szse'

    results = {}

    for year in range(start_year, end_year + 1):
        # 年报通常在次年1-4月发布
        se_date = f'{year}-01-01~{year+1}-06-30'

        data = {
            'stock': stock_param,
            'tabName': 'fulltext',
            'pageNum': 1,
            'pageSize': 10,
            'column': column,
            'category': 'category_ndbg_szsh',
            'seDate': se_date,
            'searchkey': '年度报告',
            'isHLtitle': 'true'
        }

        try:
            response = requests.post(url, data=data, timeout=15)
            result = response.json()
            announcements = result.get('announcements', [])

            if announcements:
                # 找到最新的年度报告
                for ann in announcements:
                    title = ann.get('announcementTitle', '')
                    # 排除更正稿、摘要等
                    if '年度报告' in title and '摘要' not in title and '英文' not in title:
                        pdf_url = f"http://static.cninfo.com.cn/{ann.get('adjunctUrl', '')}"
                        results[year] = pdf_url
                        break

            time.sleep(SLEEP_SECONDS * 0.5)  # 短间隔

        except Exception as e:
            print(f"    [警告] {stock_code} {year}年 年报链接获取失败: {e}")

    return results


def download_pdf(url: str, save_path: str) -> bool:
    """下载PDF文件"""
    import requests

    try:
        response = requests.get(url, timeout=60, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        return False
    except Exception as e:
        print(f"    [警告] PDF下载失败: {e}")
        return False


def extract_text_from_pdf(pdf_path: str, max_pages: int = 100) -> str:
    """从PDF提取文本（限制页数避免内存溢出）"""
    try:
        import pdfplumber

        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages[:max_pages]):
                if True:
                    page_text = page.extract_text()
                    if page_text:
                        text_parts.append(page_text)

        return '\n'.join(text_parts)
    except ImportError:
        print("    [错误] 需要安装 pdfplumber: pip install pdfplumber")
        return ""
    except Exception as e:
        print(f"    [警告] PDF文本提取失败: {e}")
        return ""


def extract_esg_sections(text: str) -> Dict[str, str]:
    """
    从年报全文中提取ESG相关章节。
    返回 {章节名: 章节文本} 字典。
    """
    sections = {}

    # 定义章节标题模式
    section_patterns = {
        "环境": r'(?:第[一二三四五六七八九十]+节|（[一二三四五六七八九十]+）)\s*(?:环境|环保|绿色|生态|节能减排|可持续发展)[^。]{0,50}',
        "社会责任": r'(?:第[一二三四五六七八九十]+节|（[一二三四五六七八九十]+）)\s*(?:社会责任|员工|公益|社区|可持续发展)[^。]{0,50}',
        "公司治理": r'(?:第[一二三四五六七八九十]+节|（[一二三四五六七八九十]+）)\s*(?:公司治理|治理结构|董事会|监事会)[^。]{0,50}',
        "合规与风险": r'(?:第[一二三四五六七八九十]+节|（[一二三四五六七八九十]+）)\s*(?:合规|风险|内部控制|风险管理)[^。]{0,50}'
    }

    for section_name, pattern in section_patterns.items():
        matches = list(re.finditer(pattern, text))
        if matches:
            # 取第一个匹配的位置，提取后续2000字符作为章节内容
            start_pos = matches[0].start()
            section_text = text[start_pos:start_pos + 5000]
            sections[section_name] = section_text

    return sections


def score_esg(text: str, sections: Dict[str, str]) -> Tuple[Dict[str, float], List[Dict]]:
    """
    对文本进行ESG评分。
    返回 (scores_dict, evidence_list)
    """
    scores = {"E_score": 0, "S_score": 0, "G_score": 0}
    evidence = []

    full_text = text + ' '.join(sections.values())

    for dimension, categories in ESG_KEYWORDS.items():
        dimension_score = 0
        dimension_evidence = []

        for category, keywords in categories.items():
            category_score = 0
            matched_keywords = []

            for keyword in keywords:
                # 计算关键词出现次数
                count = len(re.findall(re.escape(keyword), full_text))
                if count > 0:
                    category_score += min(count, 3)  # 每个关键词最多3分
                    matched_keywords.append(keyword)

                    # 记录证据
                    # 查找关键词所在位置的上下文
                    idx = full_text.find(keyword)
                    if idx >= 0:
                        context_start = max(0, idx - 50)
                        context_end = min(len(full_text), idx + 100)
                        context = full_text[context_start:context_end].replace('\n', ' ')

                        # 判断在哪个章节
                        section_found = "全文"
                        for sec_name, sec_text in sections.items():
                            if keyword in sec_text:
                                section_found = sec_name
                                break

                        dimension_evidence.append({
                            "dimension": dimension,
                            "category": category,
                            "keyword": keyword,
                            "count": count,
                            "context": context[:150],
                            "section": section_found
                        })

            # 每个类别最高5分
            dimension_score += min(category_score, 5)

        # 每个维度满分30分，归一化到0-100
        scores[f"{dimension}_score"] = min(dimension_score * (100 / 30), 100)
        evidence.extend(dimension_evidence)

    # 计算ESG总分（加权平均）
    scores["ESG_total"] = (
        scores["E_score"] * 0.3 +
        scores["S_score"] * 0.3 +
        scores["G_score"] * 0.4
    )

    return scores, evidence


def main():
    """主函数"""
    print("=" * 60)
    print("ESG评分面板构建程序")
    print(f"数据范围: {START_YEAR}-{END_YEAR}")
    print("=" * 60)

    # 确保缓存目录存在
    os.makedirs(PDF_CACHE_DIR, exist_ok=True)

    # 加载公司列表
    companies = load_company_list()

    # 存储所有结果
    all_esg_data = []
    all_evidence = []

    # 处理每家公司
    for idx, row in companies.iterrows():
        stock_code = str(row['stock_code']).zfill(6)
        stock_name = row['stock_name']

        print(f"\n[{idx+1}/{len(companies)}] 处理: {stock_code} {stock_name}")

        # 获取年报链接
        report_urls = fetch_annual_report_urls(stock_code, START_YEAR, END_YEAR)
        print(f"  找到 {len(report_urls)} 份年报")

        # 处理每一年
        for year, pdf_url in report_urls.items():
            print(f"  [{year}] 下载年报...", end=" ", flush=True)

            # 检查缓存
            pdf_filename = f"{stock_code}_{year}.pdf"
            pdf_path = os.path.join(PDF_CACHE_DIR, pdf_filename)

            if not os.path.exists(pdf_path):
                if download_pdf(pdf_url, pdf_path):
                    print("✓", end=" ", flush=True)
                else:
                    print("✗ (下载失败)")
                    continue
            else:
                print("(缓存)", end=" ", flush=True)

            # 提取文本
            text = extract_text_from_pdf(pdf_path)
            if not text:
                print("✗ (文本提取失败)")
                continue

            # 提取ESG章节
            sections = extract_esg_sections(text)

            # ESG评分
            scores, evidence = score_esg(text, sections)

            # 记录结果
            esg_record = {
                "stock_code": stock_code,
                "stock_name": stock_name,
                "year": year,
                **scores
            }
            all_esg_data.append(esg_record)

            # 记录证据
            for ev in evidence:
                ev["stock_code"] = stock_code
                ev["stock_name"] = stock_name
                ev["year"] = year
            all_evidence.extend(evidence)

            print(f"✓ ESG={scores['ESG_total']:.1f}")

            time.sleep(SLEEP_SECONDS)

    # 生成面板数据
    if all_esg_data:
        esg_panel = pd.DataFrame(all_esg_data)
        esg_panel = esg_panel.sort_values(['stock_code', 'year']).reset_index(drop=True)
        esg_panel.to_csv(ESG_PANEL_FILE, index=False, encoding='utf-8-sig')
        print(f"\n✓ ESG面板已保存: {ESG_PANEL_FILE}")
        print(f"  记录数: {len(esg_panel)}")
        print(f"  公司数: {esg_panel['stock_code'].nunique()}")

        # 统计
        print("\nESG评分统计:")
        print(esg_panel[['E_score', 'S_score', 'G_score', 'ESG_total']].describe().round(2))

    # 生成证据日志
    if all_evidence:
        evidence_df = pd.DataFrame(all_evidence)
        evidence_df.to_csv(EVIDENCE_LOG_FILE.replace('.md', '.csv'), index=False, encoding='utf-8-sig')

        # 生成Markdown格式证据日志
        with open(EVIDENCE_LOG_FILE, 'w', encoding='utf-8') as f:
            f.write("# ESG评分证据日志\n\n")
            f.write(f"生成时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for _, ev in pd.DataFrame(all_evidence).iterrows():
                f.write(f"## {ev['stock_code']} {ev['stock_name']} - {ev['year']}年\n\n")
                f.write(f"**维度**: {ev['dimension']} | **类别**: {ev['category']}\n\n")
                f.write(f"**关键词**: {ev['keyword']} (出现 {ev['count']} 次)\n\n")
                f.write(f"**章节位置**: {ev['section']}\n\n")
                f.write(f"**原文证据**:\n> {ev['context']}\n\n")
                f.write("---\n\n")

        print(f"✓ 证据日志已保存: {EVIDENCE_LOG_FILE}")

    print("\n✓ 全部任务完成！")


if __name__ == "__main__":
    main()
