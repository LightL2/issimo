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
  },
  {
    source: 'Google',
    rating: 4.9,
    author: 'Сергей',
    text: 'Эспрессо Illy и паста карбонара — то, ради чего хочется вернуться. Отличный сервис.',
    date: '2024-04-02',
    displayDate: '2 апреля 2024',
  },
  {
    source: 'Яндекс.Карты',
    rating: 4.8,
    author: 'Давид',
    text: 'Уютный интерьер, внимательные бариста и десерты уровня Италии.',
    date: '2024-02-28',
    displayDate: '28 февраля 2024',
  },
  {
    source: 'Яндекс.Карты',
    rating: 4.7,
    author: 'Малика',
    text: 'Любимый формат семейных ужинов: спокойная музыка, дровяная пицца и детское меню.',
    date: '2024-01-18',
    displayDate: '18 января 2024',
  },
];

if (reviewsList) {
  reviewsData.forEach((review) => {
    const article = document.createElement('article');
    article.className = 'review';

    const ratingLabel = `Оценка ${review.rating.toFixed(1)} из 5`;

    article.innerHTML = `
      <div class="review__meta">
        <span class="review__source">${review.source}</span>
        <span class="review__rating" aria-label="${ratingLabel}">★ ${review.rating.toFixed(1)}</span>
      </div>
      <h3>${review.author}</h3>
      <p>${review.text}</p>
      <time datetime="${review.date}">${review.displayDate}</time>
    `;

    reviewsList.appendChild(article);
  });
}
