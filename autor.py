class Autor:
    def _init_(self, nombre, nacionalidad, nacimiento, fallecimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacimiento = nacimiento
        self.fallecimiento = fallecimiento

    def mostrar_info(self):
        print("Autor:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Nacimiento:", self.nacimiento)
        print("Fallecimiento:", self.fallecimiento)