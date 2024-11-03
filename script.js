/**
 * Función para cifrar el texto ingresado en el campo de entrada.
 * Envía una solicitud POST al servidor para realizar el cifrado.
 */
async function cifrarTexto() {
    // Obtiene el texto ingresado por el usuario en el textarea con id "inputText"
    const inputText = document.getElementById("inputText").value;

    try {
        // Realiza una solicitud POST al endpoint "/cifrar" en el servidor
        const response = await fetch("https://maquina-turing-cifrado-texto.vercel.app/cifrar", {
            method: "POST", // Método HTTP de la solicitud
            headers: {
                "Content-Type": "application/json" // Tipo de contenido de la solicitud
            },
            // Convierte el texto ingresado a formato JSON y lo envía en el cuerpo de la solicitud
            body: JSON.stringify({ text: inputText })
        });

        // Verifica si la respuesta es exitosa
        if (!response.ok) {
            throw new Error("Error en la solicitud de cifrado");
        }

        // Convierte la respuesta a formato JSON
        const data = await response.json();

        // Muestra el texto cifrado en el textarea con id "outputText"
        document.getElementById("outputText").value = data.result;
    } catch (error) {
        console.error("Error al cifrar el texto:", error);
        alert("Hubo un problema al cifrar el texto. Intenta de nuevo.");
    }
}

/**
 * Función para descifrar el texto ingresado en el campo de entrada.
 * Envía una solicitud POST al servidor para realizar el descifrado.
 */
async function descifrarTexto() {
    // Obtiene el texto ingresado por el usuario en el textarea con id "inputText"
    const inputText = document.getElementById("inputText").value;

    try {
        // Realiza una solicitud POST al endpoint "/descifrar" en el servidor
        const response = await fetch("https://maquina-turing-cifrado-texto.vercel.app/descifrar", {
            method: "POST", // Método HTTP de la solicitud
            headers: {
                "Content-Type": "application/json" // Tipo de contenido de la solicitud
            },
            // Convierte el texto ingresado a formato JSON y lo envía en el cuerpo de la solicitud
            body: JSON.stringify({ text: inputText })
        });

        // Verifica si la respuesta es exitosa
        if (!response.ok) {
            throw new Error("Error en la solicitud de descifrado");
        }

        // Convierte la respuesta a formato JSON
        const data = await response.json();

        // Muestra el texto descifrado en el textarea con id "outputText"
        document.getElementById("outputText").value = data.result;
    } catch (error) {
        console.error("Error al descifrar el texto:", error);
        alert("Hubo un problema al descifrar el texto. Intenta de nuevo.");
    }
}
