(() => {
  const siteUrl = document.getElementById('site-url');
  const backToTop = document.querySelector('.back-to-top');
  const navLinks = [...document.querySelectorAll('.primary-nav a[href^="#"]')];
  const sections = navLinks
    .map((link) => document.querySelector(link.getAttribute('href')))
    .filter(Boolean);

  if (siteUrl) {
    siteUrl.href = window.location.href.split('#')[0];
    siteUrl.textContent = siteUrl.href;
  }

  const updateBackToTop = () => {
    if (backToTop) backToTop.classList.toggle('is-hidden', window.scrollY < 360);
  };

  const updateActiveNav = () => {
    let activeSection = sections[0];
    const marker = window.scrollY + 160;

    sections.forEach((section) => {
      if (section.offsetTop <= marker) activeSection = section;
    });

    navLinks.forEach((link) => {
      link.classList.toggle('is-active', link.getAttribute('href') === `#${activeSection.id}`);
    });
  };

  window.addEventListener('scroll', () => {
    updateBackToTop();
    updateActiveNav();
  }, { passive: true });
  updateBackToTop();
  updateActiveNav();

  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const revealItems = document.querySelectorAll(
    '.section-heading, .info-card, .strength-card, .growth-note, .experience-card, .kindness-card, .activity-feature, .tech-card, .award-card, .education-card, .quote-grid blockquote'
  );
  revealItems.forEach((item) => item.classList.add('reveal'));
  document.body.classList.add('reveal-ready');

  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      currentObserver.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -24px 0px' });

  revealItems.forEach((item) => observer.observe(item));
})();
