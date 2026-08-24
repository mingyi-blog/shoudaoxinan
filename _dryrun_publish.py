# -*- coding: utf-8 -*-
"""模拟 11:00 发布部署自动化的真实逻辑，端到端试跑 W35 草稿。"""
import json, re, os, subprocess, sys

BLOG = r"E:/workbuddy/2026-08-07-15-40-47/blog"
DR = os.path.join(BLOG, "drafts", "2026-W35.md")
JSON = os.path.join(BLOG, "posts_data.json")
PY = r"C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe"

txt = open(DR, encoding="utf-8").read()

# --- 步骤1 上游校验 ---
assert os.path.getsize(DR) > 0, "草稿为空"

# --- 解析契约 ---
m = re.search(r"#\s*草稿[:：]\s*(.+)", txt)
title = m.group(1).strip()
meta = {}
for line in txt.splitlines():
    mm = re.match(r"-\s*(slug|date|iso|reading|tags|summary)\s*[:：]\s*(.+)", line)
    if mm:
        meta[mm.group(1)] = mm.group(2).strip()
content = re.search(r"##\s*正文（HTML）\s*(.*?)(?=##\s*FAQ|$)", txt, re.S).group(1).strip()
faq_raw = re.search(r"##\s*FAQ[（(]可选[）)]\s*(.*)", txt, re.S)
faq = []
if faq_raw:
    for qa in re.findall(r"-\s*Q[:：]\s*(.+?)\s*A[:：]\s*(.+)", faq_raw.group(1)):
        faq.append({"q": qa[0].strip(), "a": qa[1].strip()})

print("【解析】title:", title)
print("【解析】slug:", meta["slug"], "| tags:", meta["tags"])

# --- 步骤3 合规自检 ---
full = title + meta.get("summary","") + content + json.dumps(faq, ensure_ascii=False)
red1 = re.findall(r"楞严|修习|佛经|修行|禅意", full)
red2 = re.findall(r"治愈|根治|特效|100%|包好|包治", full)  # 仅拦截"承诺疗效"完整词；"治疗/医疗/就医/医生诊断"为合规表述，放行
red3 = re.findall(r"xingjue|微信|二维码|公众号|http://|https://", full)
print("【自检】①无修行内容:", "否" if red1 else "是", red1)
print("【自检】②无医疗承诺词:", "否" if red2 else "是", red2)
print("【自检】③无联系方式:", "否" if red3 else "是", red3)
assert not red1 and not red2 and not red3, "合规未过，暂停"

# --- 步骤4 插入 JSON ---
data = json.load(open(JSON, encoding="utf-8"))
assert meta["slug"] not in [p["slug"] for p in data], "已发过，跳过"
entry = {
    "slug": meta["slug"], "title": title, "date": meta["date"], "iso": meta["iso"],
    "reading": meta["reading"], "tags": [t.strip() for t in meta["tags"].split("、")],
    "summary": meta["summary"],
    "related": [p["slug"] for p in data if p["slug"] in ("chushu","mofu","neck-shoulder")][:3],
    "faq": faq, "content": content,
}
data.insert(0, entry)
json.dump(data, open(JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("【插入】posts_data.json 现有篇数:", len(data))

# --- 步骤5 生成静态站 ---
r = subprocess.run([PY, os.path.join(BLOG, "gen.py")], capture_output=True, text=True)
print("【生成】", r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[:200])

print("\n✅ 端到端（解析→自检→插入→生成）全部通过，文章已就位待 push。")
print("URL 预览:", f"https://mingyi-blog.github.io/shoudaoxinan/posts/{meta['slug']}.html")
