import requests
from obra import Obra
from artista import Artista
import csv


##    Clase principal del sistema MetroArt. Permite buscar y mostrar obras del museo por diferentes criterios: departamento, nacionalidad y artista.
class Galeria:


    # Inicializa las listas para almacenar obras, departamentos y nacionalidades.
    def __init__(self):

        self.obras = []
        self.departamentos = []
        self.nacionalidades = []

    # Carga la lista de nacionalidades desde el archivo CSV.
    def cargar_nacionalidades(self):
       
        try:
            with open("CH_Nationality_List_20171130_v1.csv", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    if fila and fila[0].strip() != "":
                        self.nacionalidades.append(fila[0].strip())
        except:
            print("No se pudo cargar el archivo de nacionalidades.")


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
        departamentos = requests.get(url)
        try:
            datos = departamentos.json()
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
        
        
        
    #Muestra la lista de nacionalidades y permite buscar obras según la nacionalidad del artista.
    def buscar_por_nacionalidad(self):
        if not self.nacionalidades:
            self.cargar_nacionalidades()

        print("\nLista de nacionalidades:")
        
        #Este for lo hice para poder imprimir la lista del csv de nacionalidad con el id correspondiente
        for i, nac in enumerate(self.nacionalidades):
            print(f"{i + 1}. {nac}")

        seleccion = input("Ingrese el número de la nacionalidad: ")
        #Usamos de las funciuones isdigit() para tartar de valdiar los ids. 
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(self.nacionalidades):
            nacionalidad = self.nacionalidades[int(seleccion) - 1]
            #Esta Url la usamos de la informacion que tiene la pagina del api, donde buscamos la nacionalidad, esta info esta en el aparatdo de Seacrh de la documentacion
            url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistNationality=true&q={nacionalidad}"
            self._buscar_y_mostrar_obras(url)
        else:
            print("Selección inválida.")


    #Solicita el nombre del artista y busca obras relacionadas.
    def buscar_por_artista(self):
        nombre = input("Ingrese el nombre del artista: ").strip()
        if nombre == "":
            print("Nombre vacío.")
            return
        #Esta Url la usamos de la informacion que tiene la pagina del api, donde buscamos el nombre del artista, esta info esta en el aparatdo de Seacrh de la documentacion
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistDisplayName=true&q={nombre}"
        self._buscar_y_mostrar_obras(url)

    #Realiza la búsqueda de obras desde una URL, las muestra de 15 en 15 y permite al usuario ver detalles de las obras. 
    #Buscamos de 15 en 15 porque en cierto punto dejaba de correr el programa. 
    def _buscar_y_mostrar_obras(self, url):
        print("Buscando obras...")
        obra_a_buscar = requests.get(url)
        try:
            data = obra_a_buscar.json()
        except:
            print("No se pudo procesar la respuesta del servidor.")
            return

        ids = data.get("objectIDs", [])
        
        if not ids:
            print("No se encontraron obras disponibles.")
            return

        self.obras = []
        index = 0
        
        #Hicimos la bsuqueda para entender mejor el range bsucamos en google aqui dejamos el link donde nos dio lka guia de este codigo: https://es.stackoverflow.com/questions/551127/c%C3%B3mo-puedo-limitar-las-entradas-de-datos-en-un-bucle-python
        while index < len(ids):
            obras_bloque = []
            for id in range(index, min(index + 15, len(ids))):
                obra_data = self._obtener_detalle_obra(ids[id])
                if obra_data:
                    self.obras.append(obra_data)
                    obras_bloque.append(obra_data)
                    obra_data.mostrar_info_basica()
                else:
                    print(f"No se pudo cargar la obra con ID {ids[id]}")

            ver_detalle = input("¿Desea ver el detalle de una de estas obras? (s/n): ")
            if ver_detalle.lower() == "s":
                id_deseado = input("Ingrese el ID de la obra: ")
                for obra in obras_bloque:
                    if str(obra.id_obra) == id_deseado:
                        obra.mostrar_info_detallada()
                    
                else:
                    print("ID no encontrado en las obras mostradas.")

            index += 15
            if index < len(ids):
                cont = input("¿Desea ver más obras? (s/n): ")
                if cont.lower() != "s":
                    break

    #    Obtiene los detalles de una obra a partir de su ID y devuelve un objeto Obra.
    #    Si la información es incompleta o la respuesta del API es inválida, retorna None.
    def _obtener_detalle_obra(self, id_obra):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}"
        obra = requests.get(url)
        try:
            obra_final = obra.json()
        except:
            return None

        if "title" not in obra_final:
            return None
        if obra_final["title"] == "":
            return None

        if "artistDisplayName" in obra_final and obra_final["artistDisplayName"] != "":
            nombre = obra_final["artistDisplayName"]
        else:
            nombre = "Desconocida"
        if "artistNationality" in obra_final and obra_final["artistNationality"] != "":
            nacionalidad = obra_final["artistNationality"]
        else:
            nacionalidad = "Desconocida"

        if "artistBeginDate" in obra_final and obra_final["artistBeginDate"] != "":
            nacimiento = obra_final["artistBeginDate"]
        else:
            nacimiento = "N/A"

        if "artistEndDate" in obra_final and obra_final["artistEndDate"] != "":
            fallecimiento = obra_final["artistEndDate"]
        else:
            fallecimiento = "N/A"

        artista = Artista(
            nombre=nombre,
            nacionalidad=nacionalidad,
            nacimiento=nacimiento,
            fallecimiento=fallecimiento
        )

        if "classification" in obra_final and obra_final["classification"] != "":
            tipo = obra_final["classification"]
        else:
            tipo = "Sin tipo"

        if "objectDate" in obra_final and obra_final["objectDate"] != "":
            fecha = obra_final["objectDate"]
        else:
            fecha = "Sin fecha"

        if "primaryImage" in obra_final and obra_final["primaryImage"] != "":
            imagen_url = obra_final["primaryImage"]
        else:
            imagen_url = "No tiene "

        return Obra(
            id_obra=id_obra,
            titulo=obra_final["title"],
            artista=artista,
            tipo=tipo,
            fecha=fecha,
            imagen_url=imagen_url
        )


    def mostrar_detalle_obra(self):
        """
        Permite al usuario ver los detalles completos de una obra si conoce su ID.
        """
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
        else:
            print("No se encontró la obra.")
            
            
            

