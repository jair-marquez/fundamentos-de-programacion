#muesta el panel principal de opciones dentro del programa
def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    
#guarda el saludo personalizado del usuario
def opcion_saludar() -> None:
    Nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {Nombre}! Bienvenido/a.")

#"a" y "b" guardan los numeros que introduzca el usuario y los suma
def opcion_suma() -> None:
    try:
        A = float(input("Primer número: "))
        B = float(input("Segundo número: "))
        print(f"La suma es: {A + B}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

#genera un a tabla de multiplicar especifica
def opcion_tabla() -> None:
    Numero = 5
    print(f"\nTabla del {Numero}:")
    for i in range(1, 11):
        print(f"{Numero} × {i} = {Numero * i}")


# ---------- Bucle principal ----------
Continuar = True              
while Continuar:
    mostrar_menu()             
    Eleccion = input("Elige una opción: ").strip()

    if Eleccion == "1":
        opcion_saludar()
    elif Eleccion == "2":
        opcion_suma()
    elif Eleccion == "3":
        opcion_tabla()
    elif Eleccion == "0":
        print("\n ¡Hasta luego!")
        Continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")