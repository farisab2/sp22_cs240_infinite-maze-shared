import json
import os
import random
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

MG_NAME = 'MG1'

with open('../config.json', 'r') as f:
  config = json.load(f)
MAIN_URL = config['main_url']
MAIN_PORT = config['main_port']
app = Flask(__name__)

load_dotenv()
port = int(os.getenv('FLASK_RUN_PORT'))
data = {'name': MG_NAME, 'url': f'{MAIN_URL}:{port}', 'author': "team-farghai"}
requests.put(f'{MAIN_URL}:{MAIN_PORT}/addMG', data=json.dumps(data), headers={'Content-Type': 'application/json'})
# Route for maze generation:
@app.route('/generate',methods=["GET"])
def GET_mg1():
  response = jsonify({"geom": ["9aa2aac", "59aaaa4", "51aa8c5", "459a651", "553ac55", "559a655", "3638a26"]})
  response.headers["Cache-Control"] = "max-age=3600"
  response.headers["Age"] = 0
  return response, 200
 