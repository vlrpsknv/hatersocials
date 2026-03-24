import html

# Read current file
with open('jensen_huang_content.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = ''.join(lines[:165])
footer = ''.join(lines[472:])

threads = [
    {'tag': 'contrarian proof', 'text': "Самые дорогие партнерства в мире работают без контракта.\n\nNvidia и TSMC. 4 триллиона долларов с одной стороны, монополия на производство чипов с другой. Между ними нет юридического документа. Только доверие, построенное за 30 лет.\n\nА ты NDA на 40 страниц подписываешь чтобы показать макет в фигме.", 'label': '#tech'},
    {'tag': 'punch line', 'text': "Интеллект скоро будет бесплатным. Вкус никогда.", 'label': '#ai'},
    {'tag': 'contrarian proof', 'text': "У CEO компании на 4 триллиона долларов 60 прямых подчиненных. Ноль встреч один на один.\n\nУ твоего тимлида 6 человек в команде и календарь забит на три недели вперед.", 'label': '#management'},
    {'tag': 'mini-story', 'text': "В 2007 году Nvidia приняла решение, которое аналитики назвали самоубийством. Встроили технологию CUDA в каждую видеокарту GeForce. Это убило маржу. Геймеры платили за игры, а получали суперкомпьютер, который им был не нужен.\n\nРасчет был на разработчиков. Если CUDA стоит в каждом компьютере, программисты начнут под нее писать. Бесплатно. Сами.\n\nКомпания стоила полтора миллиарда. Сейчас стоит четыре триллиона.\n\nИногда убить маржу это и есть стратегия.", 'label': '#business'},
    {'tag': 'observation', 'text': "Думать стоит в 100 раз дороже чем читать. Даже для машин.\n\nКогда AI просто читает и отвечает, это дешево. Когда он останавливается, рассуждает, проверяет себя, потребление вычислений взлетает в сотни раз. Оказывается, размышление это роскошь не только для людей.", 'label': '#ai'},
    {'tag': 'punch line', 'text': "Дата-центры больше не хранят данные. Они производят интеллект. Это уже не склады. Это фабрики.", 'label': '#tech'},
    {'tag': 'mini-story', 'text': 'Метод Дженсена Хуанга для принятия решений: систематическое забывание.\n\nПеред каждым большим решением он намеренно забывает все прошлые решения по этой теме. Не потому что они были плохие. А потому что мозг якорится на старых ответах и перестает видеть новые.\n\nПо сути, ctrl+z для мышления. Откатить не код, а собственные убеждения.', 'label': '#продуктивность'},
    {'tag': 'observation', 'text': "AI уже прочитал весь интернет. Весь. Человеческие тексты закончились.\n\nТеперь он учится на данных, которые сам же и генерирует. Синтетические данные. Машина учит машину.\n\nЗвучит как научная фантастика 2015 года, но это буквально происходит прямо сейчас.", 'label': '#ai'},
    {'tag': 'punch line', 'text': "Один AI запускает сотни копий себя для решения одной задачи. А тебя на собесе спрашивают умеешь ли ты работать в команде.", 'label': '#ai'},
    {'tag': 'observation', 'text': 'Дженсен Хуанг не управляет людьми. Он управляет убеждениями.\n\n60 директоров. Никаких личных встреч. Вместо этого он формирует систему координат, в которой люди сами принимают правильные решения.\n\nМенеджмент как операционная система, а не как ручное управление.', 'label': '#management'},
    {'tag': 'observation', 'text': 'Все боятся что AI заберет работу. А надо бояться другого.\n\nИнтеллект становится commodity. "Я умный" перестанет быть преимуществом. Останется только "мне не все равно."', 'label': '#ai'},
    {'tag': 'narrative judo', 'text': "Мы думаем что ИИ это что-то воздушное, в облаке. Нет. Один серверный шкаф NVIDIA весит 2 тонны и состоит из 1.3 миллиона компонентов. Это тяжелая промышленность. Просто с интерфейсом чат-бота.", 'label': '#tech'},
]

x_posts = [
    {'tag': 'punch line', 'text': "Intelligence is about to be free. Taste never will be."},
    {'tag': 'contrarian proof', 'text': "The most valuable partnership in tech has no contract.\n\nNVIDIA ($4T) and TSMC (monopoly on chip manufacturing). No legal document between them. Just 30 years of trust.\n\nMeanwhile your startup needs a 40-page NDA to share a pitch deck."},
    {'tag': 'punch line', 'text': "Jensen Huang has 60 direct reports and zero 1-on-1 meetings.\n\nYour manager has 5 reports and no open calendar slots until April."},
    {'tag': 'mini-story', 'text': "In 2007, NVIDIA made a decision Wall Street called suicidal.\n\nThey put CUDA, a parallel computing platform, into every GeForce gaming GPU. Gamers didn't need it. It crushed margins. Analysts panicked.\n\nThe bet: if CUDA is on every machine, developers will build on it for free.\n\nNVIDIA was worth $1.5B then. Today: $4T.\n\nDestroying your margins is sometimes the strategy."},
    {'tag': 'punch line', 'text': "Thinking costs 100x more than reading. Even for machines."},
    {'tag': 'observation', 'text': "AI has read the entire internet. All of it. Human-generated text is exhausted.\n\nNow it trains on data it generates itself. Synthetic data. Machines teaching machines.\n\nThis sounded like sci-fi in 2015. It's infrastructure planning in 2026."},
    {'tag': 'punch line', 'text': 'One AI spawns hundreds of copies of itself to solve a single problem.\n\nAnd they ask you in interviews if you\'re a "team player."'},
    {'tag': 'mini-story', 'text': "Jensen Huang's decision-making method: systematic forgetting.\n\nBefore every major decision, he deliberately forgets all previous decisions on that topic. Not because they were wrong. Because the brain anchors to old answers and stops seeing new ones.\n\nCtrl+Z for your own beliefs.\n\nMost teams do the opposite. \"We already decided this in Q3.\" That's not wisdom. That's anchoring bias with a calendar date."},
    {'tag': 'observation', 'text': "Data centers used to store information. Warehouses for bytes.\n\nNow they produce intelligence. They're factories.\n\nThat one word change, warehouse to factory, is a $4 trillion insight."},
    {'tag': 'punch line', 'text': "Jensen Huang doesn't manage people. He manages belief systems."},
    {'tag': 'observation', 'text': "Four scaling laws of AI:\n\nReading. More data, smarter model.\nAugmentation. AI generates its own training data.\nThinking. Spend 100x compute to reason, not just respond.\nMultiplication. One AI spawns teams of sub-agents.\n\nEach one is a separate order of magnitude. Stack all four and you understand why NVIDIA is building factories, not servers."},
    {'tag': 'observation', 'text': "NVIDIA's Vera Rubin rack: 1.3 million components, 2 tons, shipped fully assembled.\n\nIt's not a computer. It's an industrial machine that manufactures intelligence."},
    {'tag': 'punch line', 'text': 'AI will replace the average. It will amplify the exceptional.\n\nThe gap between "good enough" and "genuinely great" is about to become a canyon.'},
    {'tag': 'reframe', 'text': 'Jensen\'s first question about any process: "What\'s the speed of light for this?" Not how fast is it now. What\'s the theoretical maximum. Then work backward. Most teams never even ask.'},
]

linkedin = [
    {'tag': 'story', 'text': 'In 2006, a GPU company made a decision that nearly killed it.\n\nThey put CUDA on every consumer gaming card. Margins collapsed. Market cap hit $1.5 billion.\n\nBut millions of developers got free GPU computing. Deep learning was born on those exact GPUs.\n\nThat company is now worth $4 trillion.\n\nThe lesson isn\'t "take big risks." It\'s more specific: know which asset compounds over decades, then sacrifice everything else to build it.\n\nFor NVIDIA, that asset was developers writing code for their platform who would never switch. Not the silicon. Not the patents. The people.\n\nWhat are you building that will still compound in 2040?\n\nSource in comments.', 'label': '#Strategy #AI #ProductDesign'},
    {'tag': 'label the unnamed', 'text': '"Thinking is harder than reading."\n\nReading: models scan the internet, absorb patterns, generate text. Cheap.\n\nThinking: models reason, plan, check their own logic during inference. 100x more compute.\n\nThat\'s why the company selling GPUs is worth $4 trillion while model companies race to cut prices. The bottleneck isn\'t who has the best model. It\'s who has enough compute to let models actually think.\n\nFor product builders: the AI features you ship today are "reading" features. Autocomplete. Summarization. The next generation involves thinking. And it costs 100x more to run.\n\nIf your pricing model assumes AI gets cheaper every year, reconsider.\n\nSource in comments.', 'label': '#AI #ProductDesign #ScalingLaws'},
    {'tag': 'contrarian proof', 'text': 'Most product teams improve things. The best ones forget things.\n\nJensen Huang calls it "systematic forgetting." Deliberately let go of past solutions because they anchor your thinking to a local maximum.\n\nNot "how do we improve v2?" but "what would we build if nothing existed?"\n\n30 years of legacy. 200+ suppliers. And they still start from zero each cycle. Every two years, a new architecture that makes the previous one obsolete.\n\nThe hardest constraint to question is always the one you inherited without noticing. The framework from v1. The user flow that "works fine."\n\nIncremental thinking can\'t produce something 10x better. Only zero-based thinking can.\n\nSource in comments.', 'label': '#ProductDesign #FirstPrinciples'},
    {'tag': 'framework', 'text': 'AI scaling has 4 phases. Most companies are stuck in phase 1.\n\nPhase 1: Reading. More data, bigger model, smarter. GPT-3 to GPT-4.\n\nPhase 2: Augmentation. Human data ran out. Model generates its own training data.\n\nPhase 3: Thinking. Model reasons during inference. 100x more compute. This is o1, o3, Claude\'s extended thinking.\n\nPhase 4: Multiplication. One AI spawns teams of sub-agents. No single model. A system solving problems.\n\nEvery phase increases compute demand. Synthetic data is unlimited. Thinking burns exponentially more. Agents multiply everything.\n\nCompanies betting "AI will get cheaper" are betting against all four phases simultaneously.\n\nSource in comments.', 'label': '#AI #Strategy #ScalingLaws'},
]

def make_card(post, with_label=True):
    safe = html.escape(post['text'])
    parts = [
        '            <div class="social-card glass rounded-xl p-4 glass-hover cursor-pointer" onclick="copyPost(this)">',
        f'                <div class="flex items-center justify-between mb-2"><span class="hook-tag">{post["tag"]}</span><span class="copy-btn text-xs text-neutral-600 px-2 py-1 rounded-md">copy</span></div>',
        f'                <p class="text-sm text-neutral-300 leading-relaxed whitespace-pre-line" data-post="{safe}">{safe}</p>',
    ]
    if with_label and 'label' in post:
        parts.append(f'                <p class="text-[10px] text-neutral-600 mt-2">{post["label"]}</p>')
    parts.append('            </div>')
    return '\n'.join(parts)

def make_li_card(post):
    safe = html.escape(post['text'])
    return f'''            <div class="social-card glass rounded-xl p-5 glass-hover cursor-pointer" onclick="copyPost(this)">
                <div class="flex items-center justify-between mb-3"><span class="hook-tag">{post['tag']}</span><span class="copy-btn text-xs text-neutral-600 px-2 py-1 rounded-md">copy</span></div>
                <p class="text-[13px] text-neutral-300 leading-relaxed whitespace-pre-line" data-post="{safe}">{safe}</p>
                <p class="text-[10px] text-neutral-600 mt-3">Comment: link + {post['label']}</p>
            </div>'''

threads_html = '\n\n'.join(make_card(p) for p in threads)
x_html = '\n\n'.join(make_card(p, False) for p in x_posts)
li_html = '\n\n'.join(make_li_card(p) for p in linkedin)

posts_section = f'''
    <!-- Social Posts v4 — Editorial Director + QA audit -->
    <div class="max-w-5xl mx-auto px-6 py-10">
        <div class="flex items-center justify-between mb-6">
            <h2 class="text-lg font-bold text-white">Social Posts <span class="text-neutral-600 font-normal text-sm ml-2">30 posts, click to copy</span></h2>
        </div>
        <div class="flex gap-2 mb-6 flex-wrap">
            <button onclick="showTab('threads')" class="tab-btn active text-sm px-4 py-2 rounded-lg text-neutral-400">Threads (12)</button>
            <button onclick="showTab('x')" class="tab-btn text-sm px-4 py-2 rounded-lg text-neutral-400">X / Twitter (14)</button>
            <button onclick="showTab('linkedin')" class="tab-btn text-sm px-4 py-2 rounded-lg text-neutral-400">LinkedIn (4)</button>
        </div>
        <div id="tab-threads" class="tab-content active space-y-3">
{threads_html}
        </div>
        <div id="tab-x" class="tab-content space-y-3">
{x_html}
        </div>
        <div id="tab-linkedin" class="tab-content space-y-4">
{li_html}
        </div>
    </div>
'''

header = header.replace('Content Pack v2', 'Content Pack v4')
header = header.replace('18 posts + podcast + report + slides + infographic', '30 posts + podcast + report + slides + infographic')

with open('jensen_huang_content.html', 'w', encoding='utf-8') as f:
    f.write(header + posts_section + footer)

print('Done!')
