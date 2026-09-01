const tabs = document.querySelectorAll('.tab');
const forms = document.querySelectorAll('.auth-form');
const requestedTab = new URLSearchParams(window.location.search).get('tab');

if (requestedTab === 'register') {
  const registerTab = document.querySelector('[data-target="register"]');
  registerTab?.click();
}

tabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.target;

    tabs.forEach((item) => {
      item.classList.toggle('active', item === tab);
      item.setAttribute('aria-selected', String(item === tab));
    });

    forms.forEach((form) => {
      form.classList.toggle('active', form.id === `${target}-form`);
    });
  });
});
