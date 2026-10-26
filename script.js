(() => {
  const siteUrl = document.getElementById('site-url');
  const backToTop = document.querySelector('.back-to-top');
  const storyLink = document.querySelector('[data-story-link]');
  const stageButtons = [...document.querySelectorAll('[data-stage]')];
  const highschoolPortfolio = document.getElementById('highschool-portfolio');
  const universityPortfolio = document.getElementById('university-portfolio');

  const activateStage = (stage, updateHistory = false) => {
    const isUniversity = stage === 'university';
    highschoolPortfolio.hidden = isUniversity;
    universityPortfolio.hidden = !isUniversity;

    stageButtons.forEach((button) => {
      const isActive = button.dataset.stage === stage;
      button.classList.toggle('is-active', isActive);
      button.setAttribute('aria-selected', String(isActive));
      button.tabIndex = isActive ? 0 : -1;
    });

    if (updateHistory) history.replaceState(null, '', isUniversity ? '#university' : '#home');
    window.scrollTo({ top: 0, behavior: 'auto' });
  };

  stageButtons.forEach((button) => {
    button.addEventListener('click', () => activateStage(button.dataset.stage, true));
  });

  if (storyLink) {
    storyLink.addEventListener('click', (event) => {
      event.preventDefault();
      document.querySelector('#story').scrollIntoView({ behavior: 'smooth' });
    });
  }

  if (siteUrl) {
    siteUrl.href = window.location.href.split('#')[0];
    siteUrl.textContent = siteUrl.href;
  }

  const updateBackToTop = () => {
    if (backToTop) backToTop.classList.toggle('is-hidden', window.scrollY < 360);
  };

  window.addEventListener('scroll', updateBackToTop, { passive: true });
  updateBackToTop();
  activateStage(location.hash === '#university' ? 'university' : 'highschool');

  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const revealItems = document.querySelectorAll(
    '.section-heading, .info-card, .strength-card, .growth-note, .experience-card, .kindness-card, .activity-feature, .tech-card, .award-card, .story-chapter, .story-weekly'
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
