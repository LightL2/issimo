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

const reviewsList = document.getElementById('reviews-list');

const serperApiKey = reviewsList?.dataset?.serperKey;

const renderReview = (review) => {
  const article = document.createElement('article');
  article.className = 'review';

  const ratingLabel = `Оценка ${review.rating.toFixed(1)} из 5`;

  article.innerHTML = `
    <a class="review__link" href="${review.url}" target="_blank" rel="noopener">
      <div class="review__header">
        <img class="review__avatar" src="${review.photo}" alt="Фото ${review.author}" loading="lazy" />
        <div>
          <div class="review__meta">
            <span class="review__source">${review.source}</span>
            <span class="review__rating" aria-label="${ratingLabel}">★ ${review.rating.toFixed(1)}</span>
          </div>
          <h3>${review.author}</h3>
        </div>
      </div>
      <p>${review.text}</p>
      <div class="review__footer">
        <time datetime="${review.date}">${review.displayDate}</time>
        <span class="review__cta">Читать отзыв →</span>
      </div>
    </a>
  `;

  reviewsList.appendChild(article);
};

const renderNotice = (message) => {
  const article = document.createElement('article');
  article.className = 'review review--notice';
  article.innerHTML = `<p>${message}</p>`;
  reviewsList.appendChild(article);
};

const formatDate = (dateString) => {
  const formatter = new Intl.DateTimeFormat('ru', { day: 'numeric', month: 'long', year: 'numeric' });
  return formatter.format(new Date(dateString));
};

const parseReviewPayload = (payload) => {
  const timeValue = payload.time
    ? payload.time * 1000
    : payload?.date?.value
    ? Number(payload.date.value) * 1000
    : Date.now();

  return {
    source: payload.source || payload.provider || 'Google',
    rating: payload.rating || payload.stars || 0,
    author: payload.author_name || payload.user || payload.reviewer || 'Гость',
    text: payload.text || payload.snippet || payload.comment || '',
    date: new Date(timeValue).toISOString().slice(0, 10),
    displayDate: formatDate(timeValue),
    photo:
      payload.profile_photo_url ||
      payload.avatar ||
      payload.photo ||
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=200&q=80&fm=webp',
    url: payload.link || payload.review_url || payload.url || payload.sourceUrl || '#',
  };
};

const loadReviews = async () => {
  if (!reviewsList) return;

  reviewsList.innerHTML = '';

  if (!serperApiKey) {
    renderNotice(
      'Для загрузки живых отзывов добавьте бесплатный ключ Serper.dev в атрибут data-serper-key или воспользуйтесь ссылками в блоке без JavaScript.'
    );
    return;
  }

  try {
    const response = await fetch('https://google.serper.dev/places', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-KEY': serperApiKey,
      },
      body: JSON.stringify({
        q: "Caffee'issimo Tashkent",
        gl: 'uz',
        hl: 'ru',
      }),
    });

    if (!response.ok) {
      renderNotice('Не удалось получить данные об отзывах. Проверьте ключ или попробуйте позже.');
      return;
    }

    const json = await response.json();
    const reviews = json?.reviews || json?.placeReviews || [];

    if (!reviews.length) {
      renderNotice('К сожалению, отзывы не найдены.');
      return;
    }

    reviews.slice(0, 6).forEach((review) => {
      renderReview(parseReviewPayload(review));
    });
  } catch (error) {
    console.error('Reviews load error', error);
    renderNotice('Не удалось загрузить отзывы. Попробуйте обновить страницу позже.');
  }
};

loadReviews();
