from maquina_turing import MaquinaDeTuring

def main():
    # Creamos una instancia de la máquina de Turing con un desplazamiento de 3
    maquina = MaquinaDeTuring(desplazamiento=3)
    
    # Texto de ejemplo
    texto_original = "DIEGO"
    print("Texto Original:", texto_original)
    
    # Cifrado
    texto_cifrado = maquina.cifrar(texto_original)
    print("Texto Cifrado:", texto_cifrado)
    
    # Desencriptado
    texto_descifrado = maquina.descifrar(texto_cifrado)
    print("Texto Descifrado:", texto_descifrado)

if __name__ == "__main__":
    main()
