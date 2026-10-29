(() => {
  const siteUrl = document.getElementById('site-url');
  const backToTop = document.querySelector('.back-to-top');
  const storyLink = document.querySelector('[data-story-link]');
  const stageButtons = [...document.querySelectorAll('[data-stage]')];
  const highschoolPortfolio = document.getElementById('highschool-portfolio');
  const universityPortfolio = document.getElementById('university-portfolio');
  const portfolioSidebar = document.querySelector('.portfolio-sidebar');
  const portfolioLinks = [...document.querySelectorAll('[data-portfolio-link]')];

  const activatePortfolioLink = (sectionId) => {
    portfolioLinks.forEach((link) => {
      const isActive = link.dataset.portfolioLink === sectionId;
      link.classList.toggle('is-active', isActive);
      if (isActive) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };

  const activateStage = (stage, updateHistory = false) => {
    const isUniversity = stage === 'university';
    highschoolPortfolio.hidden = isUniversity;
    universityPortfolio.hidden = !isUniversity;
    portfolioSidebar.hidden = isUniversity;
    document.body.classList.toggle('has-portfolio-sidebar', !isUniversity);

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

  portfolioLinks.forEach((link) => {
    link.addEventListener('click', () => activatePortfolioLink(link.dataset.portfolioLink));
  });

  const portfolioSections = portfolioLinks
    .map((link) => document.getElementById(link.dataset.portfolioLink))
    .filter(Boolean);
  if ('IntersectionObserver' in window) {
    const portfolioObserver = new IntersectionObserver((entries) => {
      const visibleSection = entries.find((entry) => entry.isIntersecting);
      if (visibleSection) activatePortfolioLink(visibleSection.target.id);
    }, { rootMargin: '-20% 0px -70% 0px' });
    portfolioSections.forEach((section) => portfolioObserver.observe(section));
  }

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
