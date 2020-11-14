from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from controllers.controller import Book, AllBooks
  
app = Flask(__name__) 
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(AllBooks, '/books/')
api.add_resource(Book, '/book/<string:author>/<string:title>/')

@app.route('/<path:string>', methods=['POST', 'GET', 'PATCH', 'DELETE']) 
def default_message_for_wrong_paths(string): 
    return jsonify({ "message": "Forbidden" }), 403
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 