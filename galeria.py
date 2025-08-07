import requests
from obra import Obra
from artista import Artista
from PIL import Image
import csv

#    Clase principal del sistema MetroArt. Permite buscar y mostrar obras del museo por diferentes criterios: departamento, nacionalidad y artista.
class Galeria:

    # Inicializa las listas para almacenar obras, departamentos y nacionalidades.
    def _init_(self):

        self.obras = []
        self.departamentos = []
        self.nacionalidades=[]

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