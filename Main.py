from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return f'Широта: {lat}, Доглота: {lon}'
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка:  {e}'

key = '585e58759bff461d93c336a542e525b6'
city = 'Эквадор'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')
