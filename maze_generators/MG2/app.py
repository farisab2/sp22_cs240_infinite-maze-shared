from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for maze generation:
@app.route('/MG2',methods=["GET"])
def GET_mg2():
  response = jsonify({"geom": ["d98088c", "51aaaa4", "51aa8c5", "049a651", "553ac55", "559a655", "3638a26"]})
  response.headers["Cache-Control"] = "max-age=3600"
  response.headers["Age"] = 0
  return response, 200