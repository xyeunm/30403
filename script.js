(() => {
  const siteUrl = document.getElementById('site-url');
  const backToTop = document.querySelector('.back-to-top');
  const navLinks = [...document.querySelectorAll('.primary-nav a[href^="#"]')];
  const tabPanels = navLinks
    .map((link) => document.querySelector(link.getAttribute('href')))
    .filter(Boolean);

  if (siteUrl) {
    siteUrl.href = window.location.href.split('#')[0];
    siteUrl.textContent = siteUrl.href;
  }

  const updateBackToTop = () => {
    if (backToTop) backToTop.classList.toggle('is-hidden', window.scrollY < 360);
  };

  const activateTab = (id, updateHistory = false) => {
    const activePanel = tabPanels.find((panel) => panel.id === id);

    tabPanels.forEach((panel) => {
      const isActive = panel === activePanel;
      panel.hidden = !isActive;
    });

    navLinks.forEach((link) => {
      const isActive = link.getAttribute('href') === `#${id}`;
      link.classList.toggle('is-active', isActive);
      link.setAttribute('aria-selected', String(isActive));
      link.tabIndex = isActive ? 0 : -1;
    });

    if (updateHistory) history.replaceState(null, '', `#${id}`);
    window.scrollTo({ top: 0, behavior: 'auto' });
  };

  navLinks.forEach((link, index) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      activateTab(link.getAttribute('href').slice(1), true);
    });
    link.addEventListener('keydown', (event) => {
      if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const offset = event.key === 'ArrowRight' ? 1 : -1;
      const nextLink = navLinks[(index + offset + navLinks.length) % navLinks.length];
      nextLink.focus();
      activateTab(nextLink.getAttribute('href').slice(1), true);
    });
  });

  window.addEventListener('scroll', updateBackToTop, { passive: true });
  window.addEventListener('hashchange', () => {
    const targetId = location.hash.slice(1);
    if (tabPanels.some((panel) => panel.id === targetId)) activateTab(targetId);
  });

  updateBackToTop();
  const initialId = tabPanels.some((panel) => panel.id === location.hash.slice(1))
    ? location.hash.slice(1)
    : 'about';
  activateTab(initialId);

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
