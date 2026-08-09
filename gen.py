# -*- coding: utf-8 -*-
import os

BASE = r"E:/workbuddy/2026-08-07-15-40-47/blog"

SITE = {
    "title": "手到心安 · 理疗与修行手记",
    "sub": "以手法疗身，以经教养心",
    "author": "明一",
    "footer": "手到心安 · 旺存理疗馆　|　文章内容仅供参考，具体身体问题请当面咨询专业人士",
}

# 7 篇文章（顺序即首页展示顺序，最新在前）
posts = [
    {
        "slug": "neck-shoulder",
        "title": "低头族的肩颈，三个手法帮它松下来",
        "date": "2026 年 8 月 9 日",
        "reading": "4 分钟",
        "tags": ["疼痛调理", "传统手法"],
        "summary": "来看理疗馆的，肩颈比腰还多。慢性僵硬先让肩颈松下来，再配合三个自用手法。",
        "content": """
<p>来看理疗馆的，这两年肩颈比腰还多。不是偶然——手机、电脑，人人都低着头，一低就是大半天。</p>
<p>先说清楚：<strong>急性的、摔过的、伴随手麻无力的，先去医院检查确认，别自己硬弄。</strong>下面这三个，是给那种「酸胀僵硬、低头加重」的慢性肩颈紧用的。</p>
<h2>一、先让肩颈「松口气」</h2>
<p>很多人肩颈疼，是因为胸锁乳突肌、斜方肌上束一直绷着，加上头往前探，颈椎压力翻倍。</p>
<ul>
<li>坐正，下巴微收，像后脑勺贴墙的感觉</li>
<li>做几次缓慢的肩耸起—沉下的动作，把肩膀「卸」下来</li>
<li>每次三到五分钟，比乱揉强</li>
</ul>
<blockquote>肩颈不是揉好的，是先「松」下来的。</blockquote>
<h2>二、三个自用手法</h2>
<ol>
<li><strong>掌根揉风池</strong>：双手拇指按在脑后发际两侧凹陷（风池），缓慢画圈，力度以「酸胀但不疼」为准，每侧一两分钟。</li>
<li><strong>提捏肩井</strong>：用拇指和食指捏住肩头最高处（肩井）的肉，轻轻向上提揉，像把耸着的肩「放」下来，重复十来次。</li>
<li><strong>指尖梳颈后</strong>：十指微屈，从发际沿颈椎两侧向下轻梳，像梳头一样，把紧绷的筋脉一点点梳开。</li>
</ol>
<p>做完会觉得后颈像卸了块砖，头也轻了。</p>
<h2>三、日常别做这三件事</h2>
<ul>
<li>长低头刷手机，颈椎悬空受力</li>
<li>枕头过高或过低，脖子整晚拧着</li>
<li>久坐不换姿势，上背肌肉缺血僵硬</li>
</ul>
<p>肩颈的问题，多半是「用错了」而不是「用多了」。我给人调肩颈，最后都会教他怎么看手机、怎么睡。手法是帮一把，日常的用法才是根本。</p>
<p>这也像修行——<strong>外面的法子帮你一时，自己的觉照管你一世。</strong></p>
""",
    },
    {
        "slug": "anqiao-daoyin",
        "title": "什么是按跷导引：一双手，陪身体慢慢松开",
        "date": "2026 年 8 月 8 日",
        "reading": "4 分钟",
        "tags": ["传统手法", "康养随笔"],
        "summary": "按跷导引是一种不靠药、顺着身体本性的理疗。旺存理疗馆持照经营，用手法帮身体通络、松开。",
        "content": """
<p>第一次听说「按跷导引」这四个字，是翻古书时撞见的。《黄帝内经》里早把「导引按跷」算作一路古法。那时候我没多想，只觉得这四个字踏实——用手，陪身体把堵着的地方，慢慢松开。</p>
<p>后来开了旺存理疗馆，天天用手，才越做越信它。</p>
<p>说穿了，按跷导引就是一种不靠药、顺着身体本性的理疗。旺存理疗馆持照经营，做的就是理疗疏通经络——通过手法，帮身体通络、松开。推拿、按摩、揉捏、点拍，都是手上的路数；落在哪儿，落在身体不舒服、发僵的地方，把那股拧着的劲，一点点化开。</p>
<p>老辈人讲「疏通经络、推行气血」。我嘴笨，翻成自己的话：就是让紧绷的地方，松口气。</p>
<p>上手有个讲究：不掰，不顶，不跟身体较劲。手搭上去，先安静下来，去听它的节奏——哪儿僵、哪儿躲、哪儿在叹气。听明白了，再轻轻引它松开。急不得。身体不是机器，你越催它，它越拧着。</p>
<p>旺存墙上挂着我写的八个字：<strong>以人为本，以病为师。</strong>人永远大过方法。身体每一处发僵、不自在，都不是来添乱的，是来提醒我们——该慢下来了，该回头看看自己了。</p>
<p>做了这么些年，我最怕别人把它想玄了。它不神，也不玄，就是一双手，一份耐心。你身上若有哪里发僵、不自在，欢迎来旺存坐坐，或者加微信聊聊。咱们慢慢调，慢慢安。</p>
""",
    },
    {
        "slug": "cultivation",
        "title": "手法是手艺，也是修行",
        "date": "2026 年 8 月 6 日",
        "reading": "4 分钟",
        "tags": ["修行心得", "传统手法"],
        "summary": "手艺要静，修行要做。能把一件手艺做细的人，心一定不粗。身安心安，手到心安。",
        "content": """
<p>常有人问我：「你做理疗，又学佛，两样不冲突吗？」</p>
<p>我倒觉得，它们在我手里是同一件事。</p>
<h2>手艺要「静」</h2>
<p>调理一个人，你心得先静。来调理的朋友紧张，你比他更紧，那这趟就白来了。我上手前有个习惯：先调自己的呼吸，把杂念放一放，再碰对方身体。</p>
<blockquote>手是心的外延。心乱，手就飘；心定，手才有数。</blockquote>
<h2>修行要「做」</h2>
<p>反过来，修行也不是光坐着念经。给人松一遍腰、陪中风后的老人做一组引导活动，这些具体的事，本身就是修行——<strong>在琐事里练得住心。</strong></p>
<p>《楞严经》讲「反闻闻自性」，我笨解成：做事的时候，把觉照留在自己这儿，不被外境卷走。</p>
<h2>一个理疗师的日常修法</h2>
<ul>
<li><strong>上手前</strong>：调呼吸，安住当下</li>
<li><strong>调理中</strong>：觉照手感，不着急见效</li>
<li><strong>见效慢</strong>：不躁，陪身体慢慢来</li>
<li><strong>被质疑</strong>：不辩，回到本分</li>
</ul>
<blockquote>我不算修得好，只是越来越确信：能把一件手艺做细的人，心一定不粗。</blockquote>
<p>身安心安，手到心安。这八个字，算是这个号想说的全部了。</p>
""",
    },
    {
        "slug": "shurangama",
        "title": "读《楞严经》几年，最受益的一句话",
        "date": "2026 年 8 月 1 日",
        "reading": "4 分钟",
        "tags": ["楞严经", "修行心得"],
        "summary": "「迷己为物，为物所转。」越品越觉得，这句话是给普通人用的，不只是给出家人的。",
        "content": """
<p>学《楞严经》好些年了。经文长、名相多，一开始真读不进去。但有几句，越品越觉得是给普通人用的，不只是给出家人的。</p>
<h2>那句话是</h2>
<blockquote>一切众生，从无始来，迷己为物，失于本心，为物所转。</blockquote>
<p>白话一点说就是：<strong>我们把自己弄丢了，反过来被外物牵着走。</strong></p>
<h2>它怎么用在日子里</h2>
<ul>
<li>来调理的朋友喊疼，我若跟着慌，手就乱——这是「为物所转」</li>
<li>别人一句质疑，我若立刻较劲，也是「为物所转」</li>
<li>数字好看就飘，不好就看淡，还是被转</li>
</ul>
<p>《楞严》要练的，是反过来：<strong>不为物所转，而能转物。</strong>不是改变外界，是心不被它带着跑。</p>
<h2>一个实操的小法子</h2>
<p>每当心被外境勾走，我试过一个很笨但有用的办法：</p>
<ol>
<li>先停手，把注意力拉回呼吸</li>
<li>在心里确认一句：「这是外境，不是我」</li>
<li>再动手、再开口</li>
</ol>
<blockquote>就这一瞬的「回来」，练久了，人就稳了。</blockquote>
<h2>和手艺的关系</h2>
<p>给人调理，最怕心浮。心一浮，手下就没数。《楞严》教我的，不是玄理，是<strong>把手上的每一个动作，都做成「回来」的练习。</strong></p>
<p>身安，心才安；心安，手才准。这是这几年读经，给我手艺最大的馈赠。</p>
""",
    },
    {
        "slug": "diabetes",
        "title": "我自创的 2 型糖尿病调理手法，为什么有效",
        "date": "2026 年 7 月 26 日",
        "reading": "5 分钟",
        "tags": ["糖尿病手法", "传统手法"],
        "summary": "做了十多年理疗，我自创了一套针对 2 型糖尿病的手法。它调的不是糖，是身体的「运化」。",
        "content": """
<p>这是被问得最多的一个话题。先声明：<strong>手法是辅助调理，不能代替正规治疗和用药，是否调整用药请遵医嘱。</strong></p>
<p>我做理疗十多年，近几年摸索出一套针对 2 型糖尿病的手法，不少朋友反馈饭前餐后数值更平稳、乏力感减轻。下面把思路讲清楚。</p>
<h2>它调的不是「糖」，是「运化」</h2>
<p>中医讲「脾主运化」，很多 2 型糖尿病的问题，不在糖本身，而在身体「转不动」了——吃进去的养分化不成能量，堆在血里。</p>
<p>所以我的手法主线是：<strong>帮中焦（腹、背、腰）松下来、转起来。</strong></p>
<h2>手法三步走</h2>
<ol>
<li><strong>腹部轻柔摩腹</strong>：顺时针慢揉小腹，力度很轻，目的是放松腹壁、促进肠腹循环，每次五到十分钟。</li>
<li><strong>背部膀胱经疏通</strong>：沿脊柱两侧用掌根缓慢推，重点在脾俞、胃俞附近，帮「中枢」松绑。</li>
<li><strong>四肢末端引气</strong>：从手脚末端向近端轻捋，像把堵住的地方慢慢引通。</li>
</ol>
<blockquote>关键不是狠，是「稳」和「久」。每天做，比偶尔做一次猛的好。</blockquote>
<h2>为什么有人反馈有效</h2>
<p>我的理解是：手法改善了局部的循环和神经张力，身体「运化」的能力回来一点，数值就稳一点。但它<strong>不是治愈</strong>，是给身体一个重新运转的机会。</p>
<p><strong>手法能做的：</strong>放松中焦、改善循环；缓解乏力、助眠；辅助平稳数值。</p>
<p><strong>手法做不到的：</strong>替代药物；不忌口不运动也行；一招搞定。</p>
<h2>修行给的提醒</h2>
<p>做这套手法这些年，我最大的体会是：<strong>急不得。</strong>身体有它自己的节奏，你越想「马上见效」，手越容易重、心越容易乱。</p>
<p>把心安在当下这一推一揉里，手自然就准了。这大概就是我把手艺和修行连起来的地方。</p>
""",
    },
    {
        "slug": "stroke-rehab",
        "title": "脑梗后的手，怎么慢慢「唤醒」",
        "date": "2026 年 7 月 18 日",
        "reading": "5 分钟",
        "tags": ["中风舒缓", "传统手法"],
        "summary": "脑梗、脑溢血术后的手最难过的不是不能动，是指令到不了。舒缓是陪身体一点点重新认识自己。",
        "content": """
<p>家属带着朋友来的时候，最常问一句话：「这手还能不能动？」</p>
<blockquote>我的答案通常是：能，但要耐心，而且是「一点点」地能。</blockquote>
<h2>先听懂身体在说什么</h2>
<p>脑梗、脑溢血之后，半身使不上劲是常见的术后状态。手最难过——不是完全不能动，是「指令到不了」。这时候最忌两样：一是放弃，二是猛练。</p>
<blockquote>舒缓不是逼身体，是陪身体重新认识自己。</blockquote>
<h2>手法上，我怎么做</h2>
<ol>
<li><strong>从近端开始</strong>：先松肩、松肘，手才能有机会。远端（手指）直接练，往往练不出。</li>
<li><strong>被动活动防僵硬</strong>：帮着把关节轻轻活动开，防止肌肉缩短、手指蜷起来。</li>
<li><strong>引导主动动作</strong>：用轻抚、轻叩，引导对方自己试着动一下，哪怕只有一毫米。</li>
<li><strong>每天短、天天做</strong>：二十分钟比一周一次两小时有用得多。</li>
</ol>
<h2>家属能帮的，比想象中多</h2>
<ul>
<li>朋友 / 家人不急，每天试着动一点点</li>
<li>家属多鼓励，少代劳</li>
<li>调理者手法 + 教方法</li>
</ul>
<h2>一点心里话</h2>
<p>这类陪伴最考验的不是技术，是<strong>定力</strong>。见效慢，容易灰心，家属容易急躁。我常跟家属说：你把心安住，对方的手才慢慢舒展开来。</p>
<p>这跟读《楞严经》是一个道理——<strong>妄念纷飞时，先别跟着跑，回到当下那一念，路就还在。</strong></p>
""",
    },
    {
        "slug": "pain-back",
        "title": "久坐腰疼？三个手法自己就能缓解",
        "date": "2026 年 7 月 9 日",
        "reading": "4 分钟",
        "tags": ["疼痛调理", "传统手法"],
        "summary": "来看理疗馆的，十个里有六七个是腰。慢性腰紧，先让腰松下来，再配合两个自用手法。",
        "content": """
<p>来看理疗馆的，十个里有六七个是腰。不是大病，但疼起来真要命，弯腰穿鞋都费劲。</p>
<p>先说清楚：<strong>急性的、摔过的、伴随腿麻无力的，先去医院检查确认，别自己硬弄。</strong>下面这三个，是给那种「酸胀僵硬、久坐加重」的慢性腰紧用的。</p>
<h2>一、先让腰「松口气」</h2>
<p>很多人腰疼，是因为腰方肌、竖脊肌一直绷着。</p>
<ul>
<li>平躺，膝盖下垫个枕头，让腰贴住床面</li>
<li>做腹式呼吸：吸气鼓肚，呼气时故意让腰往下沉</li>
<li>每次五分钟，比乱揉强</li>
</ul>
<blockquote>腰不是揉好的，是先「松」下来的。</blockquote>
<h2>二、两个自用手法</h2>
<ol>
<li><strong>掌根按揉腰眼</strong>：手掌根贴在腰部两侧凹陷处，缓慢画圈，力度以「酸胀但不疼」为准，每侧两分钟。</li>
<li><strong>轻提髂后上棘</strong>：双手拇指和食指捏住骨盆后上缘的肉，轻轻向上提，像把腰「吊」起来一点，重复十来次。</li>
</ol>
<p>做完会觉得腰像卸了块砖。</p>
<h2>三、日常别做这三件事</h2>
<ul>
<li>瘫在沙发上刷手机，腰椎悬空受力</li>
<li>弯腰搬重物，压力全压椎间盘</li>
<li>久坐不换姿势，肌肉缺血僵硬</li>
</ul>
<p>腰的问题，多半是「用错了」而不是「用多了」。我给人调腰，最后都会教他怎么坐、怎么搬。手法是帮一把，日常的用法才是根本。</p>
<p>这也像修行——<strong>外面的法子帮你一时，自己的觉照管你一世。</strong></p>
""",
    },
    {
        "slug": "welcome",
        "title": "开篇：以手法疗身，以经教养心",
        "date": "2026 年 7 月 2 日",
        "reading": "4 分钟",
        "tags": ["康养随笔", "修行心得"],
        "summary": "做理疗十多年，我越来越觉得：治身和修心，本就是一件事。这里是我的手法与修行手记。",
        "content": """
<blockquote>做理疗十多年，我越来越觉得：治身和修心，本就是一件事。</blockquote>
<p>开这个号，是想把两件事认真写下来。</p>
<p>一件是<strong>手上的功夫</strong>。我在理疗馆做了十来年，调理过各种各样的疼痛，也陪许多脑梗、脑溢血术后的朋友用手法慢慢舒缓过来。尤其近几年，我自创了一套调理 2 型糖尿病的手法，反馈出乎意料地好。这些都不是书本能直接抄来的，是手上磨出来的。</p>
<p>另一件是<strong>心里的路</strong>。我学《楞严经》好些年了，越读越觉得，它讲的不是迷信，而是把「心」这件事说得很透。修行让我在手忙的时候不慌，在见效慢的时候不急。</p>
<h2>为什么把这两样放一起</h2>
<p>因为它们在我身上是连着的：</p>
<ul>
<li>给人调理时，先安自己的心，手才稳</li>
<li>读经时，先调好自己的身，坐得住才读得进</li>
<li>身体松了，妄念就少；心定了，手法才准</li>
</ul>
<blockquote>身不安，心难静；心不定，手不准。</blockquote>
<h2>这里会有什么</h2>
<p>我会慢慢写，主要围绕几条线：</p>
<ol>
<li><strong>疼痛调理</strong>——腰、颈、肩的常见问题，哪些能自己缓解</li>
<li><strong>中风舒缓</strong>——术后身体状态，手法怎么一点点帮上忙</li>
<li><strong>糖尿病手法</strong>——我自创的那套思路，原理解释给你听</li>
<li><strong>楞严修行</strong>——几年读经，最受益的几句话</li>
<li><strong>康养随笔</strong>——一个理疗师的生活观察</li>
</ol>
<blockquote>文章内容是我个人的经验整理，仅供参考；具体身体问题，请一定当面找专业人士评估。</blockquote>
<p>如果你也关注「身体怎么好起来、心里怎么静下来」，欢迎留下来，咱们慢慢聊。</p>
""",
    },
]

POST_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 手到心安</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <h1 class="site-title">手到心安</h1>
    <p class="site-sub">以手法疗身，以经教养心</p>
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
    <a class="back-home" href="../">← 返回首页</a>
  </article>
</main>
<footer class="site-footer">{footer}</footer>
</body>
</html>
"""

INDEX_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>手到心安 · 理疗与修行手记</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <h1 class="site-title">手到心安</h1>
    <p class="site-sub">以手法疗身，以经教养心</p>
  </div>
</header>
<main class="wrap post-list">
{cards}
</main>
<footer class="site-footer">{footer}</footer>
</body>
</html>
"""


def tags_html(tags):
    return "".join('<span class="tag">{}</span>'.format(t) for t in tags)


def gen():
    os.makedirs(os.path.join(BASE, "posts"), exist_ok=True)
    # 文章页
    for p in posts:
        html = POST_TEMPLATE.format(
            title=p["title"],
            date=p["date"],
            reading=p["reading"],
            author=SITE["author"],
            content=p["content"],
            tags_html=tags_html(p["tags"]),
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
    index_html = INDEX_TEMPLATE.format(cards=cards, footer=SITE["footer"])
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("generated:", len(posts), "posts + index.html")


if __name__ == "__main__":
    gen()
