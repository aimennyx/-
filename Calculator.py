#Калькулятор
from colorama import init
from colorama import Fore, Back, Style

print( Back.CYAN )
print ( Fore.RED )
what = input("Какую операцию выполняем? (+, -, *, /): ")

a = float( input("Введите первое число: "))
b = float( input("Введите второе число: "))

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == '-':
	c = a - b
	print("Результат: " + str(c))	
elif what == '*':
	c = a * b
	print("Результат: " + str(c))	
elif what == '/':
	c = a / b
	print("Результат: " + str(c))
else: 
	print("Введена неверная операция")
input()	


temp = w.temperature('celsius')['temp']

	answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status,", температура в районе " + str(temp) + ".\n\n"

	if temp < 10:
		answer += "Сейчас там холодно, лучше пососать хуйца"
	elif temp < 20:
		answer += "Холодновато там, однако. Лучше пососать хуйца"
	else:
		answer += "Погодка просто шик, можно соснуть хуйца!"

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
