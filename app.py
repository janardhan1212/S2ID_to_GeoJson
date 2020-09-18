from flask import Flask
from flask_restful import Api

from resources.S2idToGeojson import S2idToGeojson

app = Flask(__name__)
api = Api(app)

api.add_resource(S2idToGeojson, "/S2idToGeojson")

if __name__ == "__main__":
  app.run()
