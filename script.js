(() => {
  const siteUrl = document.getElementById('site-url');
  const githubRow = document.getElementById('github-row');
  const githubLink = document.getElementById('github-link');
  const backToTop = document.querySelector('.back-to-top');

  siteUrl.href = `${window.location.origin}${window.location.pathname}`;
  siteUrl.textContent = siteUrl.href;

  // Set this URL directly when deploying through a custom domain or another host.
  const repositoryUrl = '';
  let inferredRepositoryUrl = '';
  if (window.location.hostname.endsWith('.github.io')) {
    const owner = window.location.hostname.split('.')[0];
    const repository = decodeURIComponent(window.location.pathname.split('/').filter(Boolean)[0] || `${owner}.github.io`);
    inferredRepositoryUrl = `https://github.com/${owner}/${repository}`;
  }
  const resolvedRepositoryUrl = repositoryUrl || inferredRepositoryUrl;
  if (resolvedRepositoryUrl) {
    githubLink.href = resolvedRepositoryUrl;
    githubRow.hidden = false;
  }

  const updateBackToTop = () => backToTop.classList.toggle('is-hidden', window.scrollY < 360);
  window.addEventListener('scroll', updateBackToTop, { passive: true });
  updateBackToTop();
})();