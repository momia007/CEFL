
    // Fecha objetivo (Ajusta la fecha y hora según tu necesidad)
    const fechaObjetivo = new Date("July 30, 2025 09:00:00").getTime();

    function actualizarContador() {
        const ahora = new Date().getTime();
        const diferencia = fechaObjetivo - ahora;

        if (diferencia <= 0) {
            document.getElementById("countdown").innerHTML = "¡Tiempo terminado!";
            return;
        }

        const dias = Math.floor(diferencia / (1000 * 60 * 60 * 24));
        const horas = Math.floor((diferencia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutos = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
        const segundos = Math.floor((diferencia % (1000 * 60)) / 1000);

        document.getElementById("countdown").innerHTML = 
            `${dias}d ${horas}h ${minutos}m ${segundos}s`;
    }

    setInterval(actualizarContador, 1000);

