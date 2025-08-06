class SistemaMetroArt:
    def __init__(self):
        self.obras = []

    def start(self):
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú MetroArt ---")
            print("1. Ver obras por departamento")
            print("2. Ver obras por nacionalidad del autor")
            print("3. Ver obras por nombre del autor")
            print("4. Ver detalles de una obra")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                pass  # Aquí se agregará la lógica más adelante
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                print("¡Gracias por usar MetroArt!")
                break
            else:
                print("Opción inválida.")