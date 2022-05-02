from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for maze generation:
@app.route('/MG3',methods=["GET"])
def GET_mg3():
  response = jsonify({ "geom": ["9aa2aac", "59aaaa4", "51aa8c5", "418a241", "553ac55", "559a655", "3638a26"]})
  response.headers["Cache-Control"] = "max-age=3600"
  response.headers["Age"] = 0
  return response, 200