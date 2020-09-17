import flask
from flask import request, jsonify, make_response
from ciclista.DLO.CiclistaDLO import CiclistaDLO

app = flask.Flask(__name__)

PORT=3200
HOST='0.0.0.0'

INFO = {
    "languages": {
        "es":"Spanish",
        "en":"English",
        "fr":"French"
    },
    "colors":{
        "r":"red",
        "g":"green",
        "b":"blue"
    },
    "clouds":{
        "IBM":"IBM CLOUD",
        "AMAZON":"AWS",
        "MICROSOFT":"AZURE"
    }
}

@app.route('/', methods=['GET'])
def home():
    return "<h1 style='color:blue'>Teste Rest API com Flask!</h1>"

@app.errorhandler(404)
def pageNotFound(e):
    #return "<h1 style='color:red'>Erro 404: Página não encontrada!</h1>"
    return make_response(jsonify(erro_404="Página não encontrada!"), 404)

@app.route('/json')
def get_json():
    res = make_response(jsonify(INFO), 200)
    return res

@app.route('/cliente', methods=['GET'])
def crud():
    param = request.args
    nmpropertie = param.get('propertie', type=str)
    vlpropertie = []
    vlpropertie.append(param.get('value', type=str))
    action = param.get('action', type=str)
    objDlo = CiclistaDLO()
    result = None

    if param:
        res={}
        for key, value in param.items():
            res[key] = value

        #print("Parametros:", res)

    if action == 'delete': #/cliente?action=delete&propertie=id&value=4
        result = objDlo.deleteById(vlpropertie)
    elif action == 'update': #/cliente?action=update&propertie=id&value=Marco,marco@email.com,Tarmac,Road,4
        print(str(vlpropertie[0]).split(','))
        result = objDlo.updateById(str(vlpropertie[0]).split(','))
    elif action == 'insert': #/cliente?action=insert&propertie=all&value=4,Marco,marco@email.com,Tarmac,Road
        result = objDlo.insert(str(vlpropertie[0]).split(','))
    elif action == 'select':
        if nmpropertie == 'email': #/cliente?action=select&propertie=email&value=bernardo.2016@gmail.com
            result = objDlo.selectByEmail(nmpropertie, vlpropertie)
        elif nmpropertie == 'id': #/cliente?action=select&propertie=id&value=1
            result = objDlo.selectById(nmpropertie, vlpropertie)
    else:
        result = pageNotFound(404)
    result = [d.__dict__ for d in result]

    return make_response(jsonify(request=res, cliente=result), 200)

@app.route('/json/<collection>/<member>')
def get_data(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res":member}), 200)
            return res

        res = make_response(jsonify({"error":"Member not found"}), 400)
        return res

    res = make_response(jsonify({"error":"Collection not found"}), 400)
    return res

# POST Method
@app.route('/json/<collection>', methods=['POST'])
def create_collection(collection):
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({"error":"Collection already exists"}), 201)
        return res

    INFO.update({collection:req})
    res = make_response(jsonify({"message":"Collection created"}), 201)
    return res

#PUT Method
@app.route('/json/<collection>/<member>', methods=['PUT'])
def update_collection(collection, member):
    req = request.get_json()
    if collection in INFO:
        if member:
            INFO[collection][member] = req["new"]
            res = make_response(jsonify({"res":INFO[collection]}), 200)
            return res

        res = make_response(jsonify({"error":"Member not found"}), 400)
        return res

    res = make_response(jsonify({"error": "Collection not found"}), 400)
    return res

#DELETE Method
@app.route('/json/<collection>', methods=['DELETE'])
def delete_collection(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO), 200)
        return res

    res = make_response(jsonify({"error": "Collection not found"}), 400)
    return res

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
