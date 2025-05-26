
document.getElementById('presupuesto-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const form = event.target;
  const data = new FormData(form);

  fetch("{% url 'enviar_presupuesto' %}", {
    method: "POST",
    headers: {
      'X-CSRFToken': data.get('csrfmiddlewaretoken')
    },
    body: data
  })
  .then(response => response.json())
  .then(result => {
    if (result.success) {
      document.getElementById('mensaje-exito').style.display = 'block';
      form.reset();
    }
  })
  .catch(error => {
    alert('Error al enviar el formulario.');
    console.error(error);
  });
});

