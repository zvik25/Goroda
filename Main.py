from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if result:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng'],
    else:
        return 'Город не найден'


key = '585e58759bff461d93c336a542e525b6'
city = 'Moscow'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')
