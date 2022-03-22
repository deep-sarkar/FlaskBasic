from flask import Flask
from flask_restful import Api

from db.utils import connect_db
from routes import all_routes
app = Flask(__name__)
api = Api(app)


def config_app_routes():
    for route in all_routes:
        end_point = route[0]
        handler = route[1]
        api.add_resource(handler, end_point)


@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Hello World</h1>'


# Driver code
config_app_routes()
connect_db()


if __name__ == '__main__':
    app.run(debug=True, port=5001)