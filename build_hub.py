"""Build hub index.html from topics.json and per-topic posts."""
import json, html, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('topics.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

# Collect all posts from all topics
all_posts = []

# Jensen posts (from build_posts.py data, hardcoded for now)
jensen_threads = [
    "Самые дорогие партнерства в мире работают без контракта.\n\nNvidia и TSMC. 4 триллиона долларов с одной стороны, монополия на производство чипов с другой. Между ними нет юридического документа. Только доверие, построенное за 30 лет.\n\nА ты NDA на 40 страниц подписываешь чтобы показать макет в фигме.",
    "Интеллект скоро будет бесплатным. Вкус никогда.",
    "У CEO компании на 4 триллиона долларов 60 прямых подчиненных. Ноль встреч один на один.\n\nУ твоего тимлида 6 человек в команде и календарь забит на три недели вперед.",
    "Думать стоит в 100 раз дороже чем читать. Даже для машин.\n\nКогда AI просто читает и отвечает, это дешево. Когда он останавливается, рассуждает, проверяет себя, потребление вычислений взлетает в сотни раз.",
    "Дата-центры больше не хранят данные. Они производят интеллект. Это уже не склады. Это фабрики.",
    "Один AI запускает сотни копий себя для решения одной задачи. А тебя на собесе спрашивают умеешь ли ты работать в команде.",
    "Дженсен Хуанг не управляет людьми. Он управляет убеждениями.\n\n60 директоров. Никаких личных встреч. Вместо этого он формирует систему координат, в которой люди сами принимают правильные решения.",
]

jensen_x = [
    "Intelligence is about to be free. Taste never will be.",
    "The most valuable partnership in tech has no contract.\n\nNVIDIA ($4T) and TSMC (monopoly on chip manufacturing). No legal document between them. Just 30 years of trust.\n\nMeanwhile your startup needs a 40-page NDA to share a pitch deck.",
    "Jensen Huang has 60 direct reports and zero 1-on-1 meetings.\n\nYour manager has 5 reports and no open calendar slots until April.",
    "Thinking costs 100x more than reading. Even for machines.",
    "One AI spawns hundreds of copies of itself to solve a single problem.\n\nAnd they ask you in interviews if you're a \"team player.\"",
    "Jensen Huang doesn't manage people. He manages belief systems.",
    "AI will replace the average. It will amplify the exceptional.\n\nThe gap between \"good enough\" and \"genuinely great\" is about to become a canyon.",
]

for t in jensen_threads:
    all_posts.append({'text': t, 'platform': 'threads', 'topic': 'jensen-huang'})
for t in jensen_x:
    all_posts.append({'text': t, 'platform': 'x', 'topic': 'jensen-huang'})

# March 2026 posts from JSON
with open('march-2026-tech/posts.json', 'r', encoding='utf-8') as f:
    march = json.load(f)

for p in march.get('threads', []):
    all_posts.append({'text': p['text'], 'platform': 'threads', 'topic': 'march-2026-tech'})
for p in march.get('x', []):
    all_posts.append({'text': p['text'], 'platform': 'x', 'topic': 'march-2026-tech'})

# Build topic cards HTML
topic_cards = []
for t in topics:
    platforms_str = ' + '.join(f"{v} {k}" for k, v in t['platforms'].items())
    topic_cards.append(f'''
        <a href="/{t['slug']}/" class="glass rounded-2xl p-6 glass-hover transition-all block">
            <p class="text-xs text-neutral-500 mb-2">{t['date']}</p>
            <h3 class="text-white font-bold text-lg mb-1">{t['title']}</h3>
            <p class="text-neutral-400 text-sm mb-3">{t['subtitle']}</p>
            <div class="flex items-center gap-3">
                <span class="tag text-xs px-2 py-0.5 rounded-full">{t['postCount']} posts</span>
                <span class="text-xs text-neutral-500">{platforms_str}</span>
            </div>
        </a>''')

# Build post cards HTML
post_cards = []
for p in all_posts:
    safe = html.escape(p['text'])
    platform_label = {'threads': 'Threads', 'x': 'X', 'linkedin': 'LinkedIn'}[p['platform']]
    platform_color = {'threads': 'tag', 'x': 'tag-blue', 'linkedin': 'tag-purple'}[p['platform']]
    topic_label = p['topic'].replace('-', ' ').title()
    post_cards.append(f'''
            <div class="social-card glass rounded-xl p-4 glass-hover cursor-pointer" data-topic="{p['topic']}" data-platform="{p['platform']}" onclick="copyPost(this)">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="{platform_color} text-[10px] px-2 py-0.5 rounded-full">{platform_label}</span>
                        <span class="text-[10px] text-neutral-600">{topic_label}</span>
                    </div>
                    <span class="copy-btn text-xs text-neutral-600 px-2 py-1 rounded-md">copy</span>
                </div>
                <p class="text-sm text-neutral-300 leading-relaxed whitespace-pre-line" data-post="{safe}">{safe}</p>
            </div>''')

# Count
total = len(all_posts)
threads_count = sum(1 for p in all_posts if p['platform'] == 'threads')
x_count = sum(1 for p in all_posts if p['platform'] == 'x')
li_count = sum(1 for p in all_posts if p['platform'] == 'linkedin')

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hatersocials</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="shared.css">
</head>
<body class="min-h-screen">

    <div class="max-w-5xl mx-auto px-6 pt-16 pb-8">
        <h1 class="text-4xl md:text-5xl font-extrabold text-white leading-tight mb-2">hatersocials</h1>
        <p class="text-neutral-400 text-lg mb-8">Content packs distilled from tech conversations. Click to copy.</p>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-12">
            <div class="glass rounded-xl p-4 text-center">
                <p class="text-2xl font-bold text-white stat-num">{len(topics)}</p>
                <p class="text-xs text-neutral-500 mt-1">topics</p>
            </div>
            <div class="glass rounded-xl p-4 text-center">
                <p class="text-2xl font-bold text-white stat-num">{total}</p>
                <p class="text-xs text-neutral-500 mt-1">total posts</p>
            </div>
            <div class="glass rounded-xl p-4 text-center">
                <p class="text-2xl font-bold text-white stat-num">{threads_count}</p>
                <p class="text-xs text-neutral-500 mt-1">Threads</p>
            </div>
            <div class="glass rounded-xl p-4 text-center">
                <p class="text-2xl font-bold text-white stat-num">{x_count}</p>
                <p class="text-xs text-neutral-500 mt-1">X / Twitter</p>
            </div>
        </div>
    </div>

    <div class="section-line max-w-5xl mx-auto"></div>

    <div class="max-w-5xl mx-auto px-6 py-10">
        <h2 class="text-lg font-bold text-white mb-6">Content Packs</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{''.join(topic_cards)}
        </div>
    </div>

    <div class="section-line max-w-5xl mx-auto"></div>

    <div class="max-w-5xl mx-auto px-6 py-10">
        <div class="flex items-center justify-between mb-6">
            <h2 class="text-lg font-bold text-white">All Posts</h2>
            <div class="flex gap-2 flex-wrap">
                <button onclick="filterPosts('all','all')" class="tab-btn active text-xs px-3 py-1.5 rounded-lg text-neutral-400">All ({total})</button>
                <button onclick="filterPosts('all','threads')" class="tab-btn text-xs px-3 py-1.5 rounded-lg text-neutral-400">Threads ({threads_count})</button>
                <button onclick="filterPosts('all','x')" class="tab-btn text-xs px-3 py-1.5 rounded-lg text-neutral-400">X ({x_count})</button>
            </div>
        </div>
        <div id="posts-feed" class="space-y-3">
{''.join(post_cards)}
        </div>
    </div>

    <div class="max-w-5xl mx-auto px-6 py-12 text-center border-t border-neutral-900">
        <p class="text-xs text-neutral-700">hatersocials by @neirohater</p>
    </div>

    <script src="shared.js"></script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(page)

print(f'Hub built: {total} posts across {len(topics)} topics')
