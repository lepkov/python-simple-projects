# Python 3.9.7
# pyowm 3.2.0
# pyTelegramBotAPI 3.6.6
import pyowm
import telebot

owm = pyowm.OWM('your-api-key-at-https://openweathermap.org/')
bot = telebot.Telebot("TELEGRAM-BOT-API-TOKEN")

@bot.message_handler(content_types=['text'])

def send_echo(message):
    observation = owm.weather_manager().weather_at_place(message.text)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    answer = "In  " + message.text + ", the temperature is: " + str(temperature) + "°C, " + w.detailed_status + ".\n\n"
    if temperature < 10:
         answer += "Wear up your winter clothes."
    elif temperature < 20:
         answer += "Wear up your fall/spring clothes."
    else: 
    	 answer += "Wear up your summer clothes."

	#bot.reply_to(message, message.text)
bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
