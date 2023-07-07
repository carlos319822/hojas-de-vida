from Repositorios.RepositorioCargo import RepositorioCargo
from Modelos.Cargo import Cargo


class ControladorCargo():
    def __init__(self):
        self.repositorioCargo = RepositorioCargo()

    def index(self):
        return self.repositorioCargo.findAll()

    def create(self, infoCargo):
        nuevoCargo = Cargo(infoCargo)
        return self.repositorioCargo.save(nuevoCargo)

    def show(self, id):
        elCargo = Cargo(self.repositorioCargo.findById(id))
        return elCargo.__dict__

    def update(self, id, infoCargo):
        CargoActual = Cargo(self.repositorioCargo.findById(id))
        CargoActual.cargoaspirado = infoCargo["cargoaspirado"]
        CargoActual.experiencia = infoCargo["experiencia"]
        