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
  # lat = flask.request.args.get('lat')
  # lon = flask.request.args.get('lon')
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
    print ap_lat, ap_lon
    ap_pos = (ap_lat, ap_lon)
    # print ap_pos
    ap_dist = haversine(my_pos, ap_pos, miles=True)
    if ap_dist <= 5:
      print ap
      return 'Not safe'
  return 'Safe'

  @app.route 




if __name__ == '__main__':
  app.run(debug=True)
