document.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname;

  document.querySelectorAll('nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;

    if ((href === '/' && currentPath === '/') || (href !== '/' && currentPath.startsWith(href))) {
      link.classList.add('text-white');
    }
  });
});
