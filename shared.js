function copyPost(card) {
    const postEl = card.querySelector('[data-post]');
    const text = postEl.getAttribute('data-post')
        .replace(/&quot;/g, '"')
        .replace(/&amp;/g, '&')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>');
    navigator.clipboard.writeText(text).then(() => {
        const btn = card.querySelector('.copy-btn');
        btn.textContent = 'copied!';
        btn.classList.add('copied');
        setTimeout(() => {
            btn.textContent = 'copy';
            btn.classList.remove('copied');
        }, 2000);
    });
}

function showTab(name) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    document.getElementById('tab-' + name).classList.add('active');
    event.target.classList.add('active');
}

function filterPosts(topic, platform) {
    const cards = document.querySelectorAll('.social-card');
    cards.forEach(card => {
        const cardTopic = card.getAttribute('data-topic');
        const cardPlatform = card.getAttribute('data-platform');
        const matchTopic = !topic || topic === 'all' || cardTopic === topic;
        const matchPlatform = !platform || platform === 'all' || cardPlatform === platform;
        card.style.display = (matchTopic && matchPlatform) ? '' : 'none';
    });
}
