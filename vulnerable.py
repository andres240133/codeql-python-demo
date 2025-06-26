import os

def ejecutar_comando(usuario):
    print(f"Ejecutando comando para el usuario: {usuario}")
    comando = f"ping {usuario}"  # <- Riesgo de inyección de comandos
    os.system(comando)

nombre_usuario = input("Ingrese una dirección o IP para hacer ping: ")
ejecutar_comando(nombre_usuario)

