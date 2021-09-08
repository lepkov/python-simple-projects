# Python 3.9.7
# pyowm 3.2.0
# Russian version
import pyowm
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
city = input("Какой город вас интересует?: ")
owm = pyowm.OWM('Ключ-API-на-https://openweathermap.org/')
observation = owm.weather_manager().weather_at_place(city)
w = observation.weather

temperature = w.temperature('celsius')['temp']

print("В городе " + city + " сейчас температура: " + str(temperature) + "°C, " + w.detailed_status + ".")

if temperature < 10:
     print ("Оденься в зимнее.")
elif temperature < 20:
     print ("Оденья в осенневесеннее.")
else: 
	print("Оденься в летнее.")
