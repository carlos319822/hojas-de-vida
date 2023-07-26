from Repositorios.RepositorioCargo import RepositorioCargo
from Repositorios.RepositorioPersona import RepositorioPersona
from Modelos.Cargo import Cargo
from Modelos.Persona import Persona


class ControladorCargo():
    def __init__(self):
        self.repositorioCargo = RepositorioCargo()
        self.repositorioPersona = RepositorioPersona()

    def index(self):
        return self.repositorioCargo.findAll()

    def create(self,infoCargo, id_persona):
        nuevoCargo = Cargo(infoCargo)
        laPersona = Persona(self.repositorioPersona.findById(id_persona))
        nuevoCargo.persona = laPersona
        return self.repositorioCargo.save(nuevoCargo)

    def show(self, id):
        elCargo = Cargo(self.repositorioCargo.findById(id))
        return elCargo.__dict__

    def update(self, id, infoCargo):
        CargoActual = Cargo(self.repositorioCargo.findById(id))
        CargoActual.cargoaspirado = infoCargo["cargoaspirado"]
        CargoActual.experiencia = infoCargo["experiencia"]
        