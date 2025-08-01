from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return f'Широта: {lat}, Долгота: {lon}'
        else:
            return 'Город не найден.'
    except Exception as e:
        return f'Возникла ошибка: {e}'


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}:\n {coordinates}')


key = '585e58759bff461d93c336a542e525b6'

window = Tk()
window.title('Координаты городов')
window.geometry('320x100')

entry = Entry()
entry.pack()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

window.mainloop()