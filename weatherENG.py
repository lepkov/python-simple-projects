# Python 3.9.7
# pyowm 3.2.0
# English version
import pyowm
city = input("In which city do you want to know the weather?: ")
owm = pyowm.OWM('your-api-key-at-https://openweathermap.org/')
observation = owm.weather_manager().weather_at_place(city)
w = observation.weather

temperature = w.temperature('celsius')['temp']

print("In  " + city + ", the temperature is: " + str(temperature) + "°C, " + w.detailed_status + ".")

if temperature < 10:
     print ("Wear up your winter clothes.")
elif temperature < 20:
     print ("Wear up your fall/spring clothes.")
else: 
	print("Wear up your summer clothes.")
