class MaquinaDeTuring:
    def __init__(self, desplazamiento=3):
        """
        Inicializa la máquina de Turing con un valor de desplazamiento predeterminado.
        
        :param desplazamiento: El número de posiciones que se utilizarán para cifrar y descifrar el texto.
        """
        self.desplazamiento = desplazamiento  # Almacena el desplazamiento para el cifrado
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Define el alfabeto utilizado para el cifrado

    def cifrar(self, texto):
        """
        Cifra el texto utilizando la cifra de César.
        
        :param texto: El texto que se va a cifrar.
        :return: El texto cifrado.
        """
        # Convierte el texto a mayúsculas y agrega un delimitador al final
        texto = texto.upper() + "#"
        resultado = ""  # Inicializa la cadena de resultado cifrado

        for letra in texto:
            if letra in self.alfabeto:  # Verifica si la letra está en el alfabeto
                # Calcula la nueva posición cifrada aplicando el desplazamiento
                nueva_pos = (self.alfabeto.index(letra) + self.desplazamiento) % len(self.alfabeto)
                resultado += self.alfabeto[nueva_pos]  # Añade la letra cifrada al resultado
            else:
                resultado += letra  # Añade el delimitador o cualquier otro símbolo sin cambios

        return resultado  # Retorna el texto cifrado

    def descifrar(self, texto):
        """
        Descifra el texto utilizando la cifra de César.
        
        :param texto: El texto que se va a descifrar.
        :return: El texto descifrado.
        """
        # Asegura que el texto está en mayúsculas
        texto = texto.upper()
        resultado = ""  # Inicializa la cadena de resultado descifrado

        for letra in texto:
            if letra in self.alfabeto:  # Verifica si la letra está en el alfabeto
                # Calcula la nueva posición descifrada aplicando el desplazamiento inverso
                nueva_pos = (self.alfabeto.index(letra) - self.desplazamiento) % len(self.alfabeto)
                resultado += self.alfabeto[nueva_pos]  # Añade la letra descifrada al resultado
            else:
                resultado += letra  # Añade el delimitador o cualquier otro símbolo sin cambios

        return resultado.rstrip("#")  # Retorna el texto descifrado, quitando el delimitador al final
