def procesar_datos():
    user_input = input("Ingrese una operación matemática: ")
    resultado = eval(user_input)  # ← Código vulnerable
    print("Resultado:", resultado)

procesar_datos()


