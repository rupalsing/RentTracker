import json
from urllib.request import urlopen


def get_place_json(query, latitude, longitude):
    return json.load(urlopen(
        f"https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json?access_token=sk.eyJ1Ijoi"
        f"YWRpdHlhb2ZmaWNpYWxndXB0YSIsImEiOiJja2QybDZ0cHoxZWk3MndvdXdvbmFuMWFhIn0.QFLoY-"
        f"P20cH_-B-l0Tb3Xw&proximity={longitude},{latitude}"))['features'][0]


def add_store(store_name, latitude, longitude, res):
    res[store_name] = {}
    nearest_store = get_place_json(store_name, latitude, longitude)
    store_name = nearest_store['place_name']
    store_lat = nearest_store['center'][1]
    store_long = nearest_store['center'][0]
    store_dist, store_time = find_distance_between(latitude, longitude, store_lat, store_long)

    res[store_name]['name'] = store_name
    res[store_name]['lat'] = store_lat
    res[store_name]['long'] = store_long
    res[store_name]['distance'] = store_dist
    res[store_name]['time'] = store_time


def get_stores_location(latitude, longitude):
    result = {}
    add_store("Tesco", latitude, longitude, result)
    add_store("Lidl", latitude, longitude, result)
    add_store("Aldi", latitude, longitude, result)

    return result


def find_distance_between(lat, long, new_lat, new_long):
    url = f"https://api.mapbox.com/directions/v5/mapbox/walking/{long},{lat};{new_long},{new_lat}?alternatives=true&" \
          f"geometries=geojson&access_token=" \
          f"pk.eyJ1IjoiYWRpdHlhb2ZmaWNpYWxndXB0YSIsImEiOiJja2Qya29ibmQxZWNoMnRsN3ZvZmpxcW92In0.3AQC94s30jm1T2EcRcWeng"
    difference_json = json.load(urlopen(url))['routes'][0]
    distance = difference_json['distance']
    time = difference_json['duration']

    return human_readable_distance(distance), human_readable_time(time)


def human_readable_distance(meters):
    if meters > 1000:
        return f"{round(meters / 1000, 2)} KM"

    return f"{round(meters % 1000, 2)} M"


def human_readable_time(seconds):
    human_text = ""
    if seconds > 3599:
        human_text += f"{round(seconds / 3600)} h "
        seconds %= 3600
    if seconds > 59:
        human_text += f"{round(seconds / 60)} m "
        seconds %= 60
    human_text += f"{round(seconds % 60)} s"
    return human_text
