from Modelos.Certificado import Certificado
from Repositorios.RepositorioCertificado import RepositorioCertificado


class ControladorCertificado():
    def __init__(self):
        self.repositorioCertificado = RepositorioCertificado()
        print("Creando controlador Certificado")

    def index(self):
        print("Listar todos los certificados")
        return self.repositorioCertificado.findAll()

    def create(self, elCertificado):
        print("Crear Certificado")
        nuevoCertificado = Certificado(elCertificado)
        return self.repositorioCertificado.save(nuevoCertificado)

    def show(self, id):
        elCertificado = Certificado(self.repositorioCertificado.findById(id))
        return elCertificado.__dict__

    def uptade(self,id, elCertificado):
        certificadoActual = Certificado(self.repositorioCertificado.findById(id))
        certificadoActual.motivo = elCertificado["motivo"]

        return self.repositorioCertificado.save(certificadoActual)

    def delete(self,id):
        print("Eliminado Certificado", id)
        return self.repositorioCertificado.delete(id)