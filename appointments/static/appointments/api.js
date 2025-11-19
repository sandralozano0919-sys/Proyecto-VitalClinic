console.log("¡Hola, JS cargado!");

async function crearCita() {
    const nombre = document.getElementById('nombre').value;
    const tipo_documento = document.getElementById('tipo_documento').value;
    const numero_documento = document.getElementById('numero_documento').value;
    const fecha = document.getElementById('fecha').value;
    const hora = document.getElementById('hora').value;
    const especialidad = document.getElementById('especialidad').value;
    const medico = document.getElementById('medico').value;

    const token = localStorage.getItem('access_token');
    if (!token) {
        alert('Debes iniciar sesión primero');
        return;
    }

    const cita = {
        nombre,
        tipo_documento,
        numero_documento,
        fecha,
        hora,
        especialidad,
        medico
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/api/appointments/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify(cita)
        });

        if (!response.ok) {
            throw new Error('Error al crear la cita');
        }

        document.getElementById('message').innerText = '¡Cita creada con éxito!';
        // Limpiar formulario
        document.querySelectorAll('input').forEach(input => input.value = '');
    } catch (error) {
        document.getElementById('message').innerText = 'Error: ' + error.message;
        document.getElementById('message').style.color = 'red';
    }
}
