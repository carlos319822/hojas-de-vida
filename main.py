from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPersona import ControladorPersona
from Controladores.ControladorFormacion import ControladorFormacion
from Controladores.ControladorCargo import ControladorCargo


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