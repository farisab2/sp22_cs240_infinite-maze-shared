from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Route for maze generation:
@app.route('/MG4',methods=["GET"])
def GET_mg4():
  hex_string = '0123456789abcdef'
  str = "".join([random.choice(hex_string) for x in range(7)])
  hex_string1 = '0123456789abcdef'
  str1 = "".join([random.choice(hex_string) for x in range(7)])
  response = jsonify({ "geom": ["9aa2aac", "59aaaa4", str, "51aa8c5" , str1, "559a655", "3638a26"]})
  return response, 200