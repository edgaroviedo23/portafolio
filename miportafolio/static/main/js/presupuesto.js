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