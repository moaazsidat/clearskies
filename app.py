import flask
import json
import requests
import random
from haversine import haversine

app = flask.Flask(__name__)

with open('airports.json') as aiports_file:
  airports_data = json.load(aiports_file)

for ap in airports_data:
  if not (ap.get('lat') and ap.get('lon')):
    airports_data.remove(ap)

with open('drones.json') as drones_file:
  drones_data = json.load(drones_file)

with open('flights.json') as flights_file:
  flights_data = json.load(flights_file)

@app.route('/')
def home():
  return 'Welcome to Skynet'


# @app.route('/weather')
# def weather():
#   lon = flask.request.args.get('lon')
#   lat = flask.request.args.get('lat')
#   print lon, lat
#   url="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, openWeatherMapAPIKey)
#   response = requests.get(url).json()
#   return flask.jsonify(response)

@app.route('/airports')
def airports():
  # print airports_data
  # my_list = [ap for ap in airports_data if ap.get('iso') == 'CA']
  lyon = (45.7597, 4.8422)
  paris = (48.8567, 2.3508)
  pearson = (43.6777176, -79.6248197)
  custom = (43.679332, -79.612203)
  # print haversine(lyon, paris, miles=True)
  # print haversine(pearson, custom, miles=True)

  # for ap in airports_data:
    # print ap.get('iso')
  # print my_list
  return 'Bar'

@app.route('/safe')
def safe():
  lat = float(flask.request.args.get('lat'))
  lon = float(flask.request.args.get('lon'))
  my_pos = (lat, lon)
  for ap in airports_data:
    ap_lat = ap.get('lat', 0.0)
    ap_lon = ap.get('lon', 0.0)
    ap_lat = float(ap_lat)
    ap_lon = float(ap_lon)

    ap_pos = (ap_lat, ap_lon)
    ap_dist = haversine(my_pos, ap_pos, miles=True)
    if ap_dist <= 5:
      return flask.jsonify(ap)
  return flask.jsonify({'safe': True})


# Returns true if object is within the rectangle defined by the lat/lon bounds
def object_in_range(ap, min_lat, max_lat, min_lon, max_lon):
  ap_lat = float(ap.get('lat', 0.0))
  ap_lon = float(ap.get('lon', 0.0))

  if (ap_lat >= min_lat and ap_lat <= max_lat):
    if (ap_lon >= min_lon and ap_lon <= max_lon):
      return True
  return False

def flight_in_range(fl, min_lat, max_lat, min_lon, max_lon):
    fl_lat = fl["coord"][0]
    fl_lon = fl["coord"][1]
    
    if (fl_lat >= min_lat and fl_lat <= max_lat):
      if (fl_lon >= min_lon and fl_lon <= max_lon):
        return True
    return False
    
    
    
# def generate_drones(min_lat, max_lat, min_lon, max_lon):
#   test_min_lat = 43.57844659660155
#   test_max_lat = 43.897733906604834
#   print random.uniform(test_min_lat, test_max_lat)
#
#   test_min_lon = -79.52642306685448
#   test_max_lon = -79.24182560294867
#   print random.uniform(test_min_lon, test_max_lon)


@app.route('/airportsin')
def aiportsin():
  # 1: bottom left
  # 2: bottom right
  # 3: top right
  # 4: top left

  lat1 = float(flask.request.args.get('lat1'))
  lon1 = float(flask.request.args.get('lon1'))
  bl = (lat1, lon1)

  lat2 = float(flask.request.args.get('lat2'))
  lon2 = float(flask.request.args.get('lon2'))
  br = (lat2, lon2)

  lat3 = float(flask.request.args.get('lat3'))
  lon3 = float(flask.request.args.get('lon3'))
  tr = (lat3, lon3)

  lat4 = float(flask.request.args.get('lat4'))
  lon4 = float(flask.request.args.get('lon4'))
  tl  = (lat4, lon4)

  min_lat = min(bl[0], br[0], tr[0], tl[0])
  max_lat = max(bl[0], br[0], tr[0], tl[0])

  min_lon = min(bl[1], br[1], tr[1], tl[1])
  max_lon = max(bl[1], br[1], tr[1], tl[1])

  # bl_t = [43.57844659660155,-79.52642306685448]
  # br_t = [43.57844659660155,-79.24182560294867]
  # tr_t = [43.897733906604834,-79.24182560294867]
  # tl_t = [43.897733906604834,-79.52642306685448]
  # generate_drones(min_lat, max_lat, min_lon, max_lon)
  results = []
  for ap in airports_data:
    if object_in_range(ap, min_lat, max_lat, min_lon, max_lon):
      results.append(ap)

  drs = []
  for dr in drones_data:
    if object_in_range(dr, min_lat, max_lat, min_lon, max_lon):
      drs.append(dr)
      # print drs
  
  fls = []
  for fl in flights_data:
    if flight_in_range(fl, min_lat, max_lat, min_lon, max_lon):
      fls.append(fl)
      print(fls)

  return flask.jsonify(airportsin=results, dronesin=drs, flightsin=fls)



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
