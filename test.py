# import math
# from colorama import init
# from colorama import Fore, Back, Style
# init()

# import pyowm
# owm = pyowm.OWM('fae645c5d6d754285b42142916d0f660')
# mgr = owm.weather_manager()

# place = input('enter the city: ')
# observation = mgr.weather_at_place(place)
# w = observation.weather

# print('in the ' + place + ' now ' + w.detailed_status, w.wind(), w.humidity, w.temperature('celsius'))


# a = 21
# b = 5.6
# name = input('Enter your name: ')
# age = input('Enter your age: ')
#print('Hello, ' + str(name) + ', are you ' + str(age) + ' years old?')


# import math
# a = 5.65
# print(math.ceil(a))

# print(Back.YELLOW)
# print(Fore.BLACK)
# operation = input('enter the operation(\'+\';\'-\'): ')

# print(Back.CYAN)
# a = float(input('enter the first num: '))
# b = float(input('enter the second num: '))

# print(Back.BLUE)
# if operation == '+':
#     c = a + b
#     print('result: ' + str(math.ceil(c)))
# elif operation == '-':
#     c = a - b
#     print('result: ' + str(math.ceil(c)))
# else:
#     print('unknown operation')

# input()

import telebot
bot = telebot.TeleBot("1864332495:AAEk-F2qjqmrATD0Bew5A3iKVSjH2uz-B9U", parse_mode = None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	# bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)