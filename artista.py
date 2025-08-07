#Esta es la clase de los autores de las obras
class Artista:
    def _init_(self, nombre, nacionalidad, nacimiento, fallecimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacimiento = nacimiento
        self.fallecimiento = fallecimiento

    def mostrar_info(self):
        print(f"Nombre del artista: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.nacimiento}")
        print(f"Fecha de fallecimiento: {self.fallecimiento}")