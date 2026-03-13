const menuButton = document.getElementById('menuButton');
const mobileMenu = document.getElementById('mobileMenu');
const year = document.getElementById('year');

if (year) {
  year.textContent = new Date().getFullYear();
}

if (menuButton && mobileMenu) {
  menuButton.addEventListener('click', () => {
    const isHidden = mobileMenu.classList.toggle('hidden');
    menuButton.setAttribute('aria-expanded', String(!isHidden));
  });

  mobileMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      menuButton.setAttribute('aria-expanded', 'false');
    });
  });
}
