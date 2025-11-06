from flask import jsonify, Blueprint

home = Blueprint('home', __name__)

@home.route('/home', methods=['GET'])
def index():
    resp = jsonify('OK')
    resp.status_code = 200
    return resp