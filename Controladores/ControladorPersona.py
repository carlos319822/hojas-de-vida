from Modelos.Persona import Persona
from Repositorios.RepositorioPersona import RepositorioPersona


class ControladorPersona():
    def __init__(self):
        self.repositorioPersona = RepositorioPersona()
        print("Creando ControladorPersona")

    def index(self):
        print("Listar todos los estudiantes")
        return self.repositorioPersona.findAll()

    def create(self, laPersona):
        print("Crear una Persona")
        nuevaPersona = Persona(laPersona)
        return self.repositorioPersona.save(nuevaPersona)

    def show(self, id):
        laPersona = Persona(self.repositorioPersona.findById(id))
        return laPersona.__dict__

    def update(self, id, laPersona):
        personaActual = Persona(self.repositorioPersona.findById(id))
        personaActual.nombres = laPersona["nombres"]
        personaActual.apellidos = laPersona["apellidos"]
        personaActual.correo = laPersona["correo"]
        personaActual.telefono = laPersona["telefono"]
        personaActual.direccion = laPersona["direccion"]
        personaActual.ciudad = laPersona["ciudad"]
        personaActual.estadocivil = laPersona["estadocivil"]

        return self.repositorioPersona.save(personaActual)


    def delete(self, id):
        print("Eliminando persona con id", id)
        return self.repositorioPersona.delete(id)