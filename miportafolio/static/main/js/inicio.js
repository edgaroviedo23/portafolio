document.addEventListener("DOMContentLoaded", function () {

  // Función para inicializar un carrusel específico
  function initCarousel(carouselSelector, trackSelector, prevSelector, nextSelector) {
    const carousel = document.querySelector(carouselSelector);
    if (!carousel) return; // Si no existe, salir

    const track = carousel.querySelector(trackSelector);
    const images = track.querySelectorAll("img");
    const prevBtn = carousel.querySelector(prevSelector);
    const nextBtn = carousel.querySelector(nextSelector);
    let index = 0;

    function updateCarousel() {
      const width = images[0].clientWidth;
      track.style.transform = `translateX(-${index * width}px)`;
    }

    prevBtn.addEventListener("click", () => {
      index = (index - 1 + images.length) % images.length;
      updateCarousel();
    });

    nextBtn.addEventListener("click", () => {
      index = (index + 1) % images.length;
      updateCarousel();
    });

    window.addEventListener("resize", updateCarousel);
  }

  // Inicializamos cada carrusel con sus selectores correspondientes
  initCarousel(".extra-carousel", ".carousel-track", ".prev", ".next");
  initCarousel(".extra-carousel2", ".carousel-track2", ".prev2", ".next2");
  initCarousel(".extra-carousel3", ".carousel-track3", ".prev3", ".next3");
  initCarousel(".extra-carousel4", ".carousel-track4", ".prev4", ".next4");

});

document.querySelectorAll('.scroll-trigger').forEach(el => {
  el.addEventListener('click', () => {
    const targetId = el.getAttribute('data-target');
    const anchor = document.getElementById(targetId);
    if (anchor) {
      const yOffset = -100; // Cambia este valor según lo que necesites
      const y = anchor.getBoundingClientRect().top + window.pageYOffset + yOffset;

      window.scrollTo({ top: y, behavior: 'smooth' });
    }
  });
});



document.querySelectorAll('.scroll-trigger').forEach(el => {
  el.addEventListener('click', () => {
    const targetId = el.getAttribute('data-target');
    const anchor = document.getElementById(targetId);

    if (anchor) {
      const header = document.getElementById('main-header');
      const headerHeight = header ? header.offsetHeight : 0;
      const y = anchor.getBoundingClientRect().top + window.pageYOffset - headerHeight;

      window.scrollTo({ top: y, behavior: 'smooth' });
    }
  });
});

const toggleBtn = document.getElementById('toggle-theme');
const body = document.body;
const svgPath = document.querySelector('header svg path');

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('light-mode');

  if (body.classList.contains('light-mode')) {
    toggleBtn.textContent = 'Modo Oscuro';
    svgPath.style.fill = 'black';  // Cambia el color del SVG a negro
  } else {
    toggleBtn.textContent = 'Modo Claro';
    svgPath.style.fill = 'white';  // Cambia el color del SVG a blanco
  }
});


function aceptarCookies() {
    document.cookie = "cookies_aceptadas=true; max-age=" + (60*60*24*365) + "; path=/";
    document.getElementById("cookie-banner").style.display = "none";
}

function rechazarCookies() {
    document.getElementById("cookie-banner").style.display = "none";
    // Aquí podrías restringir funcionalidades si lo deseas
}