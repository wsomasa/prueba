
    // Función para actualizar la fecha y la hora
function actualizarFechaHora() {
      // Obtener la fecha y la hora actual
    var fechaHora = new Date();
      
      // Formatear la fecha y la hora como texto
    var fecha = fechaHora.toLocaleDateString();
    var hora = fechaHora.toLocaleTimeString();
      
      // Actualizar el contenido del contenedor con la fecha y la hora
    document.getElementById('banner').innerHTML = 'Fecha: ' + fecha + ' - Hora: ' + hora;
    }
    
    // Llamar a la función para actualizar la fecha y la hora cada segundo
    setInterval(actualizarFechaHora, 1000);


    
    
