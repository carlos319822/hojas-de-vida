from Modelos.Formacion import Formacion
from Repositorios.RepositorioFormacion import RepositorioFormacion


class ControladorFormacion():
    def __init__(self):
        self.repositorioFormacion = RepositorioFormacion()
        print("Creando ControladorFormacion")

    def index(self):
        return self.repositorioFormacion.findAll()

    def create(self,laFormacion):
        print("Crear una Formacion")
        nuevaFormacion = Formacion(laFormacion)
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

