from Modelos.Formacion import Formacion
from Modelos.Persona import Persona
from Repositorios.RepositorioFormacion import RepositorioFormacion
from Repositorios.RepositorioPersona import RepositorioPersona

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorFormacion():
    def __init__(self):
        self.repositorioFormacion = RepositorioFormacion()
        self.repositorioPersona = RepositorioPersona()

    def index(self):
        return self.repositorioFormacion.findAll()

    def create(self,infoFormacion, id_persona):
        nuevaFormacion = Formacion(infoFormacion)
        laPersona = Persona(self.repositorioPersona.findById(id_persona))
        nuevaFormacion.persona = laPersona
        return self.repositorioFormacion.save(nuevaFormacion)

    def show(self, id):
        laFormacion = Formacion(self.repositorioFormacion.findById(id))
        return laFormacion.__dict__

    def update(self, id, infoFormacion):
        FormacionActual = Formacion(self.repositorioFormacion.findById(id))
        FormacionActual.secundaria = infoFormacion["secundaria"]
        FormacionActual.estudios = infoFormacion["estudios"]
        FormacionActual.institucion = infoFormacion["institucion"]
        FormacionActual.estado = infoFormacion["estado"]

        return self.repositorioFormacion.save(FormacionActual)

    def delete(self, id):
        return self.repositorioFormacion.delete(id)

