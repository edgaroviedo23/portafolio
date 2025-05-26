    document.getElementById('presupuesto-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const form = event.target;
  const data = new FormData(form);

  fetch("{% url 'enviar_presupuesto' %}", {
    method: "POST",
    headers: {
      'X-CSRFToken': data.get('csrfmiddlewaretoken')  // csrf token del form
    },
    body: data
  })
  .then(response => response.json())
  .then(result => {
    if (result.success) {
      // Muestra el mensaje de éxito
      document.getElementById('mensaje-exito').style.display = 'block';
      form.reset();
    } else {
      alert('No se pudo enviar el presupuesto.');
    }
  })
  .catch(error => {
    alert('Error al enviar el formulario.');
    console.error(error);
  });
    });