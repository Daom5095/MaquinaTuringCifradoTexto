from flask import Flask, request, jsonify  # Importa Flask y funciones necesarias
from flask_cors import CORS  # Importa CORS para permitir solicitudes desde diferentes dominios
from maquina_turing import MaquinaDeTuring  # Importa la clase MaquinaDeTuring del módulo correspondiente

app = Flask(__name__)  # Crea una instancia de la aplicación Flask
CORS(app, resources={r"/*": {"origins": "*"}}) # Habilita CORS en todas las rutas para permitir solicitudes de otros orígenes
maquina = MaquinaDeTuring(desplazamiento=3)  # Crea una instancia de la máquina de Turing con un desplazamiento de 3

@app.route("/cifrar", methods=["POST"])
def cifrar():
    """
    Endpoint para cifrar texto utilizando la máquina de Turing.
    
    Este endpoint espera una solicitud POST con un JSON que contenga el texto a cifrar.
    
    :return: Un JSON con el resultado cifrado.
    """
    data = request.get_json()  # Obtiene los datos JSON de la solicitud
    texto = data.get("text", "")  # Extrae el texto a cifrar, con un valor predeterminado de cadena vacía
    resultado = maquina.cifrar(texto)  # Cifra el texto utilizando la máquina de Turing
    return jsonify({"result": resultado})  # Retorna el resultado cifrado en formato JSON

@app.route("/descifrar", methods=["POST"])
def descifrar():
    """
    Endpoint para descifrar texto utilizando la máquina de Turing.
    
    Este endpoint espera una solicitud POST con un JSON que contenga el texto a descifrar.
    
    :return: Un JSON con el resultado descifrado.
    """
    data = request.get_json()  # Obtiene los datos JSON de la solicitud
    texto = data.get("text", "")  # Extrae el texto a descifrar, con un valor predeterminado de cadena vacía
    resultado = maquina.descifrar(texto)  # Descifra el texto utilizando la máquina de Turing
    return jsonify({"result": resultado})  # Retorna el resultado descifrado en formato JSON

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración si este archivo se ejecuta directamente
