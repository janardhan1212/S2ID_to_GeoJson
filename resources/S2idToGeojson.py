import json

import geojson
import s2sphere
from flask import jsonify, request
from flask_restful import Resource


class S2idToGeojson(Resource):
  def post(self):
    decoded_response=request.data.decode("utf-8")
    parsed_data = json.loads(decoded_response)
    s2ids = parsed_data['s2ids']
    result = self.s22g(s2ids)
    return result, 200

  def get_feature(self, s):
    c = s2sphere.Cell(s2sphere.CellId(s))
    y = [s2sphere.LatLng.from_point(c.get_vertex(i)) for i in [0,1,2,3,0]]
    x = [[(x.lng().degrees, x.lat().degrees) for x in y]]

    g = geojson.Polygon(x)
    f = geojson.Feature(geometry=g, properties={'s2id':str(s), 'lvl': str(c.level())})
    return f
  def s22g(self,s2ids):
    s2 = [int(x) for x in s2ids]
    print(s2)
    lf = [self.get_feature(s) for s in s2]
    fc = geojson.FeatureCollection(lf)
    return fc
