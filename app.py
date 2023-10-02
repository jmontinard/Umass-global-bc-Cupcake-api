"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)
CORS(app)



@app.route("/")
def root():
    """Render homepage."""

    return render_template("index.html")

@app.route("/api/cupcakes")
def list_cupcakes():
    """list all cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcake=all_cupcakes)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """creates a new single cupcake"""
    new_cupcake = Cupcake(
        flavor = request.json['flavor'],
        size   = request.json['size'],
        rating = request.json['rating'],                  
        image  = request.json['image'] or None)   
                
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake = new_cupcake.serialize())
    return (response_json, 201)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcakes(cupcake_id):
    """get data on single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods = ["PATCH"])
def edit_cupcakes(cupcake_id):
    """UPDATES a cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    request.json
    cupcake.flavor = request.json['flavor'],
    cupcake.size   = request.json['size'],
    cupcake.rating = request.json['rating'],                  
    cupcake.image  = request.json['image']
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods = ["DELETE"])
def delete_cupcakes(cupcake_id):
    """DELETES a cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")