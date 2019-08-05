"""
fastcrud
@author Jeffrey Wang
"""

from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_all():
    # return everything in this database
    return jsonify({'nada'})

@app.route('/<uuid:id>', methods=['GET'])
def get_single(id):
    # return only one row from database
    return jsonify({'nada'})

@app.route('/', methods=['POST'])
def create():
    # insert new row into database
    return jsonify({'nada'})

@app.route('/<uuid:id>', methods=['PUT'])
def update(id):
    # replace one row of database
    return jsonify({'nada'})

@app.route('/<uuid:id>', methods=['DELETE'])
def delete(id):
    # delete one row of database
    return jsonify({'nada'})

# Helper methods

def generate_uuid():
    return str(uuid.uuid4())
