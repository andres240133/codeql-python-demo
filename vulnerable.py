import os

def ejecutar_comando(usuario):
    comando = f"ping {usuario}"  # <- Riesgo: el input se inserta directamente en un comando del sistema
    os.system(comando)

nombre = input("Ingrese dirección IP o dominio: ")
ejecutar_comando(nombre)


