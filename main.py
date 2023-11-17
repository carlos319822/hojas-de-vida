from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPersona import ControladorPersona
from Controladores.ControladorFormacion import ControladorFormacion
from Controladores.ControladorCargo import ControladorCargo
from Controladores.ControladorVacante import ControladorVacante
from Controladores.ContraladorExperiencia import ControladorExperiencia
from Controladores.ControladorCertificado import ControladorCertificado


app = Flask(__name__)
"""
Los cors permiten que se puedan hacer pruebas al 
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)
"""
Implementacion de los controladores
"""

miControladorPersona = ControladorPersona()
miControladorFormacion = ControladorFormacion()
miControladorCargo = ControladorCargo()
miControladorVacante = ControladorVacante()
micontroladorExperiencia = ControladorExperiencia()
miControladorCertificado = ControladorCertificado()
"""
Servicios que el servidor ofrecerá; se definen las rutas
y tipos de peticiones a las cuales el servidor responderá CRUD.
"""

#########################Servicios Persona###################################


@app.route("/personas",methods=['GET'])
def getPersonas():
    json = miControladorPersona.index()
    return jsonify(json)


@app.route("/personas",methods=['POST'])
def crearPersona():
    data = request.get_json()
    json = miControladorPersona.create(data)
    return jsonify(json)


@app.route("/personas/<string:id>",methods=['GET'])
def getPersona(id):
    json = miControladorPersona.show(id)
    return jsonify(json)


@app.route("/personas/<string:id>",methods=['PUT'])
def modificarPersona(id):
    data = request.get_json()
    json = miControladorPersona.update(id,data)
    return jsonify(json)


@app.route("/personas/<string:id>",methods=['DELETE'])
def eliminarPersona(id):
    json = miControladorPersona.delete(id)
    return jsonify(json)

##############################################################################


############################Servicios fromacion#################################

@app.route("/formacion", methods=['GET'])
def getFormaciones():
    json = miControladorFormacion.index()
    return jsonify(json)


@app.route("/formacion/<string:id>", methods=['GET'])
def getFormacion(id):
    json = miControladorFormacion.show(id)
    return jsonify(json)


@app.route("/formacion", methods=['POST'])
def crearFormacion():
    data = request.get_json()
    json = miControladorFormacion.create(data)
    return jsonify(json)


@app.route("/formacion/<string:id>", methods=['PUT'])
def modificarFormacion(id):
    data = request.get_json()
    json = miControladorFormacion.update(id, data)
    return jsonify(json)


@app.route("/formacion/<string:id>", methods=['DELETE'])
def eliminarFormacion(id):
    json = miControladorFormacion.delete(id)
    return jsonify(json)

##############################################################################


############################Servicios cargo#################################

@app.route("/cargo", methods=['GET'])
def getCargos():
    json = miControladorCargo.index()
    return jsonify(json)


@app.route("/cargo/<string:id>", methods=['GET'])
def getCargo(id):
    json = miControladorCargo.show(id)
    return jsonify(json)


@app.route("/cargo/persona/<string:id_persona>", methods=['POST'])
def crearCargo(id_persona):
    data = request.get_json()
    json = miControladorCargo.create(data, id_persona)
    return jsonify(json)


@app.route("/cargo/<string:id>", methods=['PUT'])
def modificarCargo(id):
    data = request.get_json()
    json = miControladorCargo.update(id, data)
    return jsonify(json)


@app.route("/cargo/<string:id>", methods=['DELETE'])
def eliminarCargo(id):
    json = miControladorCargo.delete(id)
    return jsonify(json)

##############################################################################


############################Servicios vacante#################################

@app.route("/vacante",methods=['GET'])
def getVacantes():
    json = miControladorVacante.index()
    return jsonify(json)


@app.route("/vacante",methods=['POST'])
def crearVacante():
    data = request.get_json()
    json = miControladorVacante.create(data)
    return jsonify(json)


@app.route("/vacante/<string:id>",methods=['GET'])
def getVacante(id):
    json = miControladorVacante.show(id)
    return jsonify(json)


@app.route("/vacante/<string:id>",methods=['PUT'])
def modificarVacante(id):
    data = request.get_json()
    json = miControladorVacante.update(id,data)
    return jsonify(json)


@app.route("/vacante/<string:id>",methods=['DELETE'])
def eliminarVacante(id):
    json = miControladorVacante.delete(id)
    return jsonify(json)

##############################################################################


############################Servicios experiencia#################################

@app.route("/experiencia",methods=['GET'])
def getExperiencias():
    json = micontroladorExperiencia.index()
    return jsonify(json)


@app.route("/experiencia",methods=['POST'])
def crearExperiencia():
    data = request.get_json()
    json = micontroladorExperiencia.create(data)
    return jsonify(json)


@app.route("/experiencia/<string:id>",methods=['GET'])
def getExperiencia(id):
    json = micontroladorExperiencia.show(id)
    return jsonify(json)


@app.route("/experiencia/<string:id>",methods=['PUT'])
def modificarExperiencia(id):
    data = request.get_json()
    json = micontroladorExperiencia.update(id,data)
    return jsonify(json)


@app.route("/experiencia/<string:id>",methods=['DELETE'])
def eliminarExperiencia(id):
    json = micontroladorExperiencia.delete(id)
    return jsonify(json)

##############################################################################


############################Servicios certificado#################################

@app.route("/certificado",methods=['GET'])
def getCertificados():
    json = miControladorCertificado.index()
    return jsonify(json)


@app.route("/certificado",methods=['POST'])
def crearCertificado():
    data = request.get_json()
    json = miControladorCertificado.create(data)
    return jsonify(json)


@app.route("/certificado/<string:id>",methods=['GET'])
def getCertificado(id):
    json = miControladorCertificado.show(id)
    return jsonify(json)


@app.route("/certificado/<string:id>",methods=['PUT'])
def modificarCertificado(id):
    data = request.get_json()
    json = miControladorCertificado.update(id,data)
    return jsonify(json)


@app.route("/certificado/<string:id>",methods=['DELETE'])
def eliminarCertificado(id):
    json = miControladorCertificado.delete(id)
    return jsonify(json)
"""
Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

"""
Método leer el archivo de configuración del proyecto,
retornará un diccionario el cual posee la información dentro del
JSON y se podrá acceder a los atributos necesarios.
"""
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])