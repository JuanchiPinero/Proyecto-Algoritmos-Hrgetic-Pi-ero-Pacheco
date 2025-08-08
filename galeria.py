#Permite al usuario ver los detalles completos de una obra si conoce su ID.
    def mostrar_detalle_obra(self):
        id_obra = input("Ingrese el ID de la obra que desea ver: ")
        if not id_obra.isdigit():
            print("ID inválido.")
            return
        obra = self._obtener_detalle_obra(int(id_obra))
        if obra:
            obra.mostrar_info_detallada()
            if obra.imagen_url:
                mostrar = input("¿Desea ver la imagen? (s/n): ")
                if mostrar.lower() == "s":
                    self._mostrar_imagen(obra.imagen_url, obra.id_obra)
