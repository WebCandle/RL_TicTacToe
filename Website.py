from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Route(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)
class JS(Resource):
    def get(self):
        headers = {'Content-Type': 'application/javascript'}
        return make_response(render_template('tictactoe.js'),200,headers)
class Style(Resource):
    def get(self):
        headers = {'Content-Type': 'text/css'}
        return make_response(render_template('style.css'),200,headers)
class Spiel(Resource):
    def get(self):
        return {'Spiel':'test'}
api.add_resource(Route, '/')
api.add_resource(Spiel, '/Spiel')
api.add_resource(JS, '/tictactoe.js')
api.add_resource(Style, '/style.css')
if __name__ == '__main__':
    app.run(debug=True)