from Modelos.Vacante import Vacante
from Repositorios.RepositorioVacante import RepositorioVacante

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorVacante():
    def __init__(self):
        self.repositorioVacante = RepositorioVacante()
        print("Creando Controlador Vacante")

    def index(self):
        print("Listar todos los estudaintes")
        return self.repositorioVacante.findAll()

    def create(self,laVacante):
        print("Creando Vacante")
        nuevaVacante = Vacante(laVacante)
        return self.repositorioVacante.save(nuevaVacante)

    def show(self,id):
        laVacante = Vacante(self.repositorioVacante.findById(id))
        return laVacante.__dict__

    def update(self,id, laVacante):
        VacanteActual = Vacante(self.repositorioVacante.findById(id))
        VacanteActual.nombre = laVacante["nombre"]
        VacanteActual.jornada = laVacante["jornada"]

        return self.repositorioVacante.save(VacanteActual)

    def delete(self, id):
        print("Eliminando Vacante", id)
        return self.repositorioVacante.delete(id)
