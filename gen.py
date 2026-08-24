# -*- coding: utf-8 -*-
import os
import json

BASE = r"E:/workbuddy/2026-08-07-15-40-47/blog"

SITE = {
    "title": "手到心安 · 理疗与康养手记",
    "sub": "以手法疗身，以养护安心",
    "author": "旺存（明一）",
    "url": "https://mingyi-blog.github.io/shoudaoxinan",
    "footer": "手到心安 · 旺存理疗馆　|　文章内容仅供参考，具体身体问题请当面咨询专业人士",
    # 媒体矩阵（把 url / handle 换成你真实的账号；保留 # 表示暂未配置）
    "social": [
        {"name": "抖音",   "handle": "@liuwangcun888",   "url": "https://www.douyin.com/user/MS4wLjABAAAA"},
        {"name": "视频号", "handle": "旺存理疗分享",     "url": "#"},
        {"name": "公众号", "handle": "待配置",           "url": "#"},
        {"name": "小红书", "handle": "待配置",           "url": "#"},
    ],
    # 私域 CTA（合规：公域不写裸微信号，仅引导至公众号/小红书私信）
    "wechat": "在公众号「手到心安」或小红书搜「旺存理疗」，关注后私信说一声，我看到都回。",
}

# 文章数据：从 posts_data.json 读取（数据归数据，代码不硬编码文章）。
# 周更自动化只需往 posts_data.json 追加一篇，再运行本脚本即可发布。
_DATA = os.path.join(BASE, "posts_data.json")
if os.path.exists(_DATA):
    with open(_DATA, encoding="utf-8") as _f:
        posts = json.load(_f)
else:
    posts = []


POST_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 手到心安</title>
<meta name="description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="手到心安">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">
{jsonld}
</script>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <h1 class="site-title">手到心安</h1>
    <p class="site-sub">以手法疗身，以养护安心</p>
    <div class="site-nav"><a href="../">首页</a></div>
  </div>
</header>
<main class="wrap article">
  <div class="article-header">
    <h1>{title}</h1>
    <div class="article-meta">{date} · {reading}阅读 · {author}</div>
  </div>
  <article class="article-body">
    {content}
    <div class="tags">{tags_html}</div>
    <div class="share-bar">
      <span class="share-tip">觉得有用，分享给需要的人：</span>
      <button class="share-btn" data-share="weibo">微博</button>
      <button class="share-btn" data-share="qq">QQ</button>
      <button class="share-btn" data-share="weixin">微信</button>
      <button class="share-btn" data-share="pyq">朋友圈</button>
      <button class="share-btn" data-share="copy">复制链接</button>
    </div>
    <div class="wx-qr" id="wx-qr" hidden></div>
    {related_html}
    {faq_html}
    {follow_block}
    {cta_block}
    <a class="back-home" href="../">← 返回首页</a>
  </article>
</main>
<footer class="site-footer">{footer}</footer>
<script src="../assets/share.js"></script>
</body>
</html>
"""

INDEX_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>手到心安 · 理疗与康养手记</title>
<meta name="description" content="手到心安是旺存理疗的康养手记，分享肩颈腰腿疼痛调理、节气养生、术后舒缓与糖尿病调理手法，附穴位与日常养护，仅供参考。">
<meta property="og:type" content="website">
<meta property="og:title" content="手到心安 · 理疗与康养手记">
<meta property="og:description" content="旺存理疗的康养手记：肩颈腰腿疼痛调理、节气养生、术后舒缓与糖尿病调理手法，附穴位与日常养护。">
<meta property="og:url" content="{site_url}/">
<meta property="og:site_name" content="手到心安">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <h1 class="site-title">手到心安</h1>
    <p class="site-sub">以手法疗身，以养护安心</p>
  </div>
</header>
<main class="wrap post-list">
{cards}
</main>
{follow_block}
{cta_block}
<footer class="site-footer">{footer}</footer>
</body>
</html>
"""


def tags_html(tags):
    return "".join('<span class="tag">{}</span>'.format(t) for t in tags)


def gen():
    os.makedirs(os.path.join(BASE, "posts"), exist_ok=True)

    # 媒体矩阵 + 私域 CTA 区块（首页与文章页共用）
    social_html = "".join(
        '<a class="social-link" href="{url}" target="_blank" rel="noopener">{name}<span>{handle}</span></a>'.format(
            url=s["url"], name=s["name"], handle=s["handle"]
        )
        for s in SITE["social"]
    )
    follow_block = (
        '<section class="follow-box">'
        '<h3 class="box-title">关注我，手法与康养常更常新</h3>'
        '<div class="social-list">' + social_html + '</div>'
        '</section>'
    )
    cta_block = (
        '<section class="cta-box">'
        '<h3 class="box-title">想私下聊聊身体？关注公众号或小红书私信我</h3>'
        '<p class="cta-text">在公众号「手到心安」或小红书搜「旺存理疗」，关注后私信说一声，我看到都回。咱们慢慢调。</p>'
        '<p class="cta-note">肩颈腰腿、术后舒缓、糖尿病调理，都可以先问一句。</p>'
        '</section>'
    )

    # slug -> title 映射，供相关阅读使用
    slug_title = {p["slug"]: p["title"] for p in posts}

    # 文章页
    for p in posts:
        related_html = ""
        if p.get("related"):
            links = "".join(
                '<a class="rel-link" href="../posts/{s}.html">{t}</a>'.format(s=s, t=slug_title.get(s, s))
                for s in p["related"]
            )
            related_html = (
                '<section class="rel-box"><h3 class="box-title">相关阅读</h3>'
                '<div class="rel-list">' + links + '</div></section>'
            )
        faq_html = ""
        if p.get("faq"):
            items = "".join(
                '<div class="faq-item"><p class="faq-q">Q：{q}</p><p class="faq-a">A：{a}</p></div>'.format(q=q, a=a)
                for q, a in p["faq"]
            )
            faq_html = '<section class="faq-box"><h3 class="box-title">大家还问</h3>' + items + '</section>'

        jsonld = json.dumps({
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": p["title"],
            "author": {"@type": "Person", "name": SITE["author"]},
            "datePublished": p["iso"],
            "description": p["summary"],
            "mainEntityOfPage": SITE["url"] + "/posts/" + p["slug"] + ".html",
            "publisher": {"@type": "Organization", "name": "手到心安"},
        }, ensure_ascii=False)

        html = POST_TEMPLATE.format(
            title=p["title"],
            description=p["summary"],
            url=SITE["url"] + "/posts/" + p["slug"] + ".html",
            jsonld=jsonld,
            date=p["date"],
            reading=p["reading"],
            author=SITE["author"],
            content=p["content"],
            tags_html=tags_html(p["tags"]),
            related_html=related_html,
            faq_html=faq_html,
            follow_block=follow_block,
            cta_block=cta_block,
            footer=SITE["footer"],
        )
        with open(os.path.join(BASE, "posts", p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
    # 首页
    cards = ""
    for p in posts:
        cards += (
            '<a class="post-card" href="posts/{slug}.html">'
            '<h2>{title}</h2>'
            '<p>{summary}</p>'
            '<div class="post-meta">{date} · {reading}阅读 · {tags}</div>'
            '</a>\n'
        ).format(
            slug=p["slug"],
            title=p["title"],
            summary=p["summary"],
            date=p["date"],
            reading=p["reading"],
            tags="、".join(p["tags"]),
        )
    index_html = INDEX_TEMPLATE.format(
        site_url=SITE["url"],
        cards=cards, follow_block=follow_block, cta_block=cta_block, footer=SITE["footer"]
    )
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # sitemap.xml
    urls = [SITE["url"] + "/"]
    for p in posts:
        urls.append(SITE["url"] + "/posts/" + p["slug"] + ".html")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += "  <url><loc>{}</loc></url>\n".format(u)
    xml += "</urlset>\n"
    with open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

    # robots.txt
    robots = "User-agent: *\nAllow: /\nSitemap: {}/sitemap.xml\n".format(SITE["url"])
    with open(os.path.join(BASE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print("generated:", len(posts), "posts + index.html + sitemap.xml + robots.txt")


if __name__ == "__main__":
    gen()
