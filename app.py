import flask
import json
import requests
from haversine import haversine

app = flask.Flask(__name__)

openWeatherMapAPIKey = "7a8668b5c3f71c0608b503bdd446c3c1"

with open('airports.json') as aiports_file:
  airports_data = json.load(aiports_file)

@app.route('/')
def home():
  return 'Welcome to Skynet'


@app.route('/weather')
def weather():
  lon = flask.request.args.get('lon')
  lat = flask.request.args.get('lat')
  print lon, lat
  url="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, openWeatherMapAPIKey)
  response = requests.get(url).json()
  return flask.jsonify(response)

@app.route('/airports')
def airports():
  # print airports_data
  # my_list = [ap for ap in airports_data if ap.get('iso') == 'CA']
  lyon = (45.7597, 4.8422)
  paris = (48.8567, 2.3508)
  pearson = (43.6777176, -79.6248197)
  custom = (43.679332, -79.612203)
  print haversine(lyon, paris, miles=True)
  print haversine(pearson, custom, miles=True)

  # for ap in airports_data:
    # print ap.get('iso')
  # print my_list
  return 'Bar'

@app.route('/safe')
def safe():
  lat = flask.request.args.get('lat')
  lon = flask.request.args.get('lon')
  # my_pos = (lat, lon)
  my_pos = (43.679332, -79.612203)
  for ap in airports_data:
    # if ap.get('lat') == None:
    #   print 'no lat', ap
    # if ap.get('lon') == None:
    #   print 'no lon', ap
    ap_lat = ap.get('lat', 0.0)
    ap_lon = ap.get('lon', 0.0)
    ap_lat = float(ap_lat)
    ap_lon = float(ap_lon)
    # print ap_lat, ap_lon
    ap_pos = (ap_lat, ap_lon)
    # print ap_pos
    ap_dist = haversine(my_pos, ap_pos, miles=True)
    if ap_dist <= 5:
      return flask.jsonify(ap)
      # return 'Not safe'
  return 'Safe'


# bl 43.610675, -79.627718
# br 43.602172, -79.331263
# tr 43.767801, -79.387859
# tl 43.752153, -79.668630

def airport_in_range(ap, bl, br, tr, tl, min_lat, max_lat, min_lon, max_lon):
  #
  # downsview = (43.74278, -79.46555)
  #
  ap_lat = float(ap.get('lat', 0.0))
  ap_lon = float(ap.get('lon', 0.0))
  ap_name = ap.get('name')
  if ap_name == 'Downsview Airport':
    print 'Yay!'

  if (ap_lat >= min_lat and ap_lat <= max_lat):
    if (ap_lon >= min_lon and ap_lon <= max_lon):
      return True
  return False

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


  print bl[0], br[0], tr[0], tl[0]
  min_lat = min(bl[0], br[0], tr[0], tl[0])
  max_lat = max(bl[0], br[0], tr[0], tl[0])

  min_lon = min(bl[1], br[1], tr[1], tl[1])
  max_lon = max(bl[1], br[1], tr[1], tl[1])

  print min_lat, max_lat, min_lon, max_lon
  # print bl, br, tr, tl

  # bl_t = [43.57844659660155,-79.52642306685448]
  # br_t = [43.57844659660155,-79.24182560294867]
  # tr_t = [43.897733906604834,-79.24182560294867]
  # tl_t = [43.897733906604834,-79.52642306685448]

  # if not bl == bl_t:
  #   print 'bl'
  #   print bl
  #   print bl_t
  #
  # if not br == br_t:
  #   print 'br'
  #   print br
  #   print br_t
  #
  # if not tr == tr_t:
  #   print 'tr'
  #
  # if not tl == tl_t:
  #   print 'tl'

  results = []
  for ap in airports_data:
    if airport_in_range(ap, bl, br, tr, tl, min_lat, max_lat, min_lon, max_lon):
      results.append(ap)
  return flask.jsonify(airportsin=results)
  return 'Bar'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
