document.addEventListener('DOMContentLoaded', function () {
  const sliders = document.querySelectorAll('.slider');

  sliders.forEach((slider) => {
    const items = slider.querySelectorAll('.slider-item');
    const prev = slider.querySelector('.slider-nav.prev');
    const next = slider.querySelector('.slider-nav.next');
    let activeIndex = 0;

    function updateSlides() {
      items.forEach((item, index) => {
        item.classList.toggle('active', index === activeIndex);
      });
    }

    if (!prev || !next || items.length === 0) {
      return;
    }

    prev.addEventListener('click', () => {
      activeIndex = (activeIndex - 1 + items.length) % items.length;
      updateSlides();
    });

    next.addEventListener('click', () => {
      activeIndex = (activeIndex + 1) % items.length;
      updateSlides();
    });
  });
});
