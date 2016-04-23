# Setup Instruction

1. Clone the repo
2. `$ cd skynet-server`
3. `$ . env/bin/activate`
4. `$ python app.py`


# Documentation

### Safe
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
