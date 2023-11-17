from Modelos.Experiencia import Experiencia
from Repositorios.RepositorioExperiencia import RepositorioExperiencia


class ControladorExperiencia():
    def __init__(self):
        self.repositorioExperiencia = RepositorioExperiencia()
        print("Creando Controlador Experiencia")

    def index(self):
        print("Listar todas las experiencias")
        return self.repositorioExperiencia.findAll()

    def create(self, laExperiencia):
        print("Creando Experiencai")
        nuevaExperiencia = Experiencia(laExperiencia)
        return self.repositorioExperiencia.save(nuevaExperiencia)

    def show(self,id):
        laExperiencia = Experiencia(self.repositorioExperiencia.findById(id))
        return laExperiencia.__dict__

    def update(self,id, laExperiencia):
        experienciaActual = Experiencia(self.repositorioExperiencia.findById(id))
        experienciaActual.empresa = laExperiencia["empresa"]

        return self.repositorioExperiencia.save(experienciaActual)


    def delete(self,id):
        print("Eliminado experiencia",id)
        return self.repositorioExperiencia.delete(id)