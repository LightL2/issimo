const navToggle = document.querySelector('.nav__toggle');
const navList = document.getElementById('nav-list');

if (navToggle && navList) {
  navToggle.addEventListener('click', () => {
    const isOpen = navList.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });

  navList.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navList.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.2,
  }
);

document.querySelectorAll('[data-animate]').forEach((element) => {
  const delay = element.getAttribute('data-delay');
  if (delay) {
    element.style.transitionDelay = `${delay}ms`;
  }
  observer.observe(element);
});

const prefersReduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (prefersReduceMotion.matches) {
  document.querySelectorAll('[data-animate]').forEach((el) => {
    el.classList.add('is-visible');
  });
  observer.disconnect();
}

const anchors = document.querySelectorAll('a[href^="#"]');
anchors.forEach((anchor) => {
  anchor.addEventListener('click', (event) => {
    const href = anchor.getAttribute('href');
    if (!href || href.length === 1) return;
    const target = document.querySelector(href);
    if (!target) return;
    event.preventDefault();
    const top = target.getBoundingClientRect().top + window.scrollY - 70;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});

const instagramFeed = document.getElementById('instagram-feed');
const instagramProfile = 'https://www.instagram.com/caffeeissimo/';
// Используем публичный web_profile_info JSON-эндпоинт Instagram через r.jina.ai
// Он выдаёт только публичные данные и не требует токена
const instagramProxy =
  'https://r.jina.ai/http://www.instagram.com/api/v1/users/web_profile_info/?username=caffeeissimo';

const shuffle = (array) => array.sort(() => Math.random() - 0.5);

const renderInstagramCard = (item) => {
  const card = document.createElement('article');
  card.className = 'insta-card';
  card.innerHTML = `
    <a class="insta-card__link" href="${item.link}" target="_blank" rel="noopener">
      <div class="insta-card__media">
        <img src="${item.image}" alt="Пост Caffee’issimo в Instagram" loading="lazy" />
      </div>
      <div class="insta-card__body">
        <p>${item.caption || 'Свежий момент из жизни Caffee’issimo.'}</p>
        <span class="insta-card__cta">Открыть пост →</span>
      </div>
    </a>
  `;
  instagramFeed.appendChild(card);
};

const renderInstagramNotice = (message) => {
  const card = document.createElement('article');
  card.className = 'insta-card insta-card--notice';
  card.innerHTML = `
    <div class="insta-card__body">
      <p>${message}</p>
      <a class="link" href="${instagramProfile}" target="_blank" rel="noopener">Перейти в Instagram</a>
    </div>
  `;
  instagramFeed.appendChild(card);
};

const loadInstagram = async () => {
  if (!instagramFeed) return;

  instagramFeed.innerHTML = '';

  try {
    const response = await fetch(instagramProxy, { cache: 'no-store' });
    if (!response.ok) throw new Error('Failed to fetch Instagram feed');

    const payload = await response.text();

    // Попытка извлечь JSON и получить медиа из профиля с корректным fallback к regex
    let items = [];

    try {
      const jsonStart = payload.indexOf('{');
      const jsonString = jsonStart >= 0 ? payload.slice(jsonStart) : '';
      const data = jsonString ? JSON.parse(jsonString) : null;

      const edges =
        data?.data?.user?.edge_owner_to_timeline_media?.edges ||
        data?.graphql?.user?.edge_owner_to_timeline_media?.edges ||
        [];

      items = edges
        .map((edge) => ({
          image: edge?.node?.display_url,
          link: edge?.node?.shortcode ? `https://www.instagram.com/p/${edge.node.shortcode}/` : null,
          caption: edge?.node?.edge_media_to_caption?.edges?.[0]?.node?.text || '',
        }))
        .filter((item) => item.image && item.link);
    } catch (error) {
      console.warn('Instagram JSON parse fallback', error);
    }

    if (!items.length) {
      const imageMatches = [...payload.matchAll(/"display_url":"([^"]+)"/g)].map((m) => m[1].replace(/\u0026/g, '&'));
      const codeMatches = [...payload.matchAll(/"shortcode":"([^"]+)"/g)].map((m) => m[1]);

      const seen = new Set();
      for (let i = 0; i < Math.min(imageMatches.length, codeMatches.length); i += 1) {
        const link = `https://www.instagram.com/p/${codeMatches[i]}/`;
        if (seen.has(link)) continue;
        seen.add(link);
        items.push({ image: imageMatches[i], link });
      }
    }

    if (!items.length) {
      renderInstagramNotice('Не удалось автоматически загрузить ленту. Откройте профиль, чтобы увидеть посты.');
      return;
    }

    shuffle(items)
      .slice(0, 6)
      .forEach((item) => renderInstagramCard(item));
  } catch (error) {
    console.error('Instagram load error', error);
    renderInstagramNotice('Лента Instagram временно недоступна. Попробуйте обновить страницу или открыть профиль.');
  }
};

loadInstagram();
