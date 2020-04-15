from flask import Flask, jsonify, request, Response
import json

from OngsModel import Ongs

from app import *

@app.route('/ongs')
def get_all_ongs():
    res = { 'ongs': Ongs.get_all_ongs() }
    return Response(json.dumps(res), status=200)

@app.route('/ongs', methods=['POST'])
def add_ong():
    req = request.get_json()
    return_data = Ongs.add_ong(req["name"], 
                               req["email"],
                               req["whatsapp"], 
                               req["city"], 
                               req["uf"])    
    return Response(json.dumps(return_data), 201, mimetype='application/json')

@app.route('/ongs/<int:id>', methods=['DELETE'])
def delete_ong(id):
  if(Ongs.delete_ong(id)):
    response = Response("", status=204)
  else:
    invalidErrorMsg = {
      "error": "Error on Ong Delete"
    }
    response = Response(json.dumps(invalidErrorMsg), 
                        status=404, mimetype='application/json')
  return response


app.run(debug=True)