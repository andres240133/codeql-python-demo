def procesar_datos():
    user_input = input("Ingrese una operación matemática: ")
    resultado = eval(user_input)  # <- eval con input: patrón peligroso
    print("Resultado:", resultado)

procesar_datos()
