# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "apartment"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "mall"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "starbucks"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for place in waypoints:
    print('{}: latitude = {},longitude = {}'.format(place["name"],place["lat"],place["lon"]))
# Add a new waypoint to the list

waypoints.append({
    "lat": 55,
    "lon": -100,
    "name": "chipotle"
})
print(waypoints)
