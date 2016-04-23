# Setup Instruction

1. Clone the repo
2. `$ cd skynet-server`
3. `$ . env/bin/activate`
4. `$ python app.py`


# Documentation

### safe
```
/safe?lat=43.679332&lon=-79.612203
```
Returns 'Safe' if there is no airport within a 5 mile radius, if not, returns the first airport that is closer than 5 miles, indicating that it is not safe

Example:
```
http://localhost:5000/safe?lat=43.679332&lon=-79.612203
```
Returns Pearson:
```
{
  continent: "NA",
  iata: "YYZ",
  iso: "CA",
  lat: "43.681583",
  lon: "-79.61146",
  name: "Lester B. Pearson International Airport",
  size: "large",
  status: 1,
  type: "airport"
}
```

### aiportsin
```
/airportsin?lat1=43.57844659660155&lon1=-79.52642306685448&lat2=43.57844659660155&lon2=-79.24182560294867&lat3=43.897733906604834&lon3=-79.24182560294867&lat4=43.897733906604834&lon4=-79.52642306685448
```
Given 4 lat long pairs where:
* lat1, lon1 – Bottom left
* lat2, lon2 – Bottom right
* lat3, lon3 – Top right
* lat4, lon4 – Top left
should return an object, where the key `airportsin` corresponds to the array of airports in the specified lat, lon rectangle

Example:
```
http://localhost:5000/airportsin?lat1=43.57844659660155&lon1=-79.52642306685448&lat2=43.57844659660155&lon2=-79.24182560294867&lat3=43.897733906604834&lon3=-79.24182560294867&lat4=43.897733906604834&lon4=-79.52642306685448
```
Returns
```

{
  "airportsin": [
    {
      "continent": "NA",
      "iata": "YKZ",
      "iso": "CA",
      "lat": "43.86131",
      "lon": "-79.36774",
      "name": "Buttonville Municipal Airport",
      "size": "medium",
      "status": 1,
      "type": "airport"
    },
    {
      "continent": "NA",
      "iata": "YTZ",
      "iso": "CA",
      "lat": "43.632023",
      "lon": "-79.39585",
      "name": "Billy Bishop Toronto City Centre Airport",
      "size": "medium",
      "status": 1,
      "type": "airport"
    },
    {
      "continent": "NA",
      "iata": "YZD",
      "iso": "CA",
      "lat": "43.74278",
      "lon": "-79.46555",
      "name": "Downsview Airport",
      "size": "medium",
      "status": 1,
      "type": "airport"
    }
  ]
}
```
