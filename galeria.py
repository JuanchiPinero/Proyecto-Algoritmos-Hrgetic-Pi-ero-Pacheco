#Muestra el menú principal del sistema y gestiona la interacción del usuario.
    def mostrar_menu(self):
        while True:
            print("\nBienvenido a MetroArt")
            print("1. Buscar obras por departamento")
            print("2. Buscar obras por nacionalidad")
            print("3. Buscar obras por nombre del artista")
            print("4. Ver detalles de una obra por ID")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.buscar_por_departamento()
            elif opcion == "2":
                self.buscar_por_nacionalidad()
            elif opcion == "3":
                self.buscar_por_artista()
            elif opcion == "4":
                self.mostrar_detalle_obra()
            elif opcion == "5":
                print("Gracias por usar MetroArt.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

#Muestra los departamentos del museo y permite buscar obras por ID de departamento.
    def buscar_por_departamento(self):
        print("\nBuscando departamentos...")
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        r = requests.get(url)
        try:
            datos = r.json()
        except:
            print("No se pudo obtener la lista de departamentos.")
            return

        self.departamentos = datos["departments"]
        for depto in self.departamentos:
            print(f"{depto['departmentId']}: {depto['displayName']}")

        depto_id = input("Ingrese el ID del departamento: ")
        if not depto_id.isdigit():
            print("ID inválido.")
            return

        url_busqueda = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={depto_id}"
        self._buscar_y_mostrar_obras(url_busqueda)

    