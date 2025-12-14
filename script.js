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

const reviewsData = [
  {
    source: 'Google',
    rating: 5,
    author: 'Алина',
    text: 'Лучшее место для завтраков в центре. Ароматный кофе и идеальные круассаны!',
    date: '2024-03-12',
    displayDate: '12 марта 2024',
    photo: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=200&q=80&fm=webp',
    url: 'https://maps.google.com/?q=Caffee%27issimo+Istiqbol+47+Tashkent',
  },
  {
    source: 'Google',
    rating: 4.9,
    author: 'Сергей',
    text: 'Эспрессо Illy и паста карбонара — то, ради чего хочется вернуться. Отличный сервис.',
    date: '2024-04-02',
    displayDate: '2 апреля 2024',
    photo: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=200&q=80&fm=webp',
    url: 'https://maps.google.com/?q=Caffee%27issimo+Amir+Temur+95A+Tashkent',
  },
  {
    source: 'Яндекс.Карты',
    rating: 4.8,
    author: 'Давид',
    text: 'Уютный интерьер, внимательные бариста и десерты уровня Италии.',
    date: '2024-02-28',
    displayDate: '28 февраля 2024',
    photo: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&q=80&fm=webp',
    url: 'https://yandex.uz/maps/?text=Caffee%27issimo%20Amir%20Temur%2095A%20%D0%A2%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82',
  },
  {
    source: 'Яндекс.Карты',
    rating: 4.7,
    author: 'Малика',
    text: 'Любимый формат семейных ужинов: спокойная музыка, дровяная пицца и детское меню.',
    date: '2024-01-18',
    displayDate: '18 января 2024',
    photo: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=200&q=80&fm=webp',
    url: 'https://yandex.uz/maps/?text=Caffee%27issimo%20Yunusabad%2084%20%D0%A2%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82',
  },
];

if (reviewsList) {
  reviewsData.forEach((review) => {
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
  });
}
