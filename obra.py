from artista import Artista


#Esta es la clase de las obras
class Obra:
    def __init__(self, id_obra, titulo, artista, tipo, fecha, imagen_url):
        self.id_obra = id_obra
        self.titulo = titulo
        self.artista = artista  
        self.tipo = tipo
        self.fecha = fecha
        self.imagen_url = imagen_url

    def mostrar_info_basica(self):
        print(f"ID: {self.id_obra} | Título: {self.titulo} | Artista: {self.artista.nombre}")

    def mostrar_info_detallada(self):
        print("\n----- DETALLE DE OBRA -----")
        print(f"Título: {self.titulo}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creación: {self.fecha}")
        self.artista.mostrar_info()
        print(f"Imagen URL: {self.imagen_url}")
