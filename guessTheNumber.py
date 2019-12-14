# Угадай число

import random       # Для генерации случайного числа

lowDigit = 10       # Нижняя граница случайного числа
highDigit = 50      # Верхняя граница случайного числа
digit = 0           # Загаданное компьютером число

countInput = 0      # Количество попыток угадать
win = False         # Угадал текущее число?
playGame = True     # Продолжается игра?
x = 0               # Число, вводимое пользователем
startScore = 100    # Начальное количество очков
score = 0           # Текущее количество очков
maxScore = 0        # Максимальное за сессию игры

# ====================================================

while (playGame):  									# Главный цикл
	digit = random.randint(lowDigit, highDigit)		# Загадываем число
	print(f'Загаданное число: {digit}')
	print('-' * 30)
	countInput = 0
	score = startScore
	print('Я загадал число, попробуйте отгадать!')

	while (not win and score > 0):			#Внутренний цикл
		print('-' * 30)
		print(f'Заработано очков: {score}')
		print(f'Рекорд: {maxScore}')

		x = ''	     						# Сбрасываем для условия в while
		while (not x.isdigit()):			# Контроль ввода числа
			x = input(f'Введите число от {lowDigit} до {highDigit}: ')
			if (not x.isdigit()):
				print('.' * 27 + 'Введите, пожалуйста, число.')

		x = int(x)

		if (x == digit):
			win = True 		# Сбрасываем win
		else:
			length = abs(x - digit)
			if (length < 3):
				print('Очень горячо!')
			elif (length < 5):
				print('Горячо!')
			elif (length < 10):
				print('Тепло')
			elif (length < 15):
				print('Прохладно')
			elif (length < 20):
				print('Холодно')
			else:
				print('Ледяной ветер')

			if (countInput == 7):
				score -= 10
				if (digit % 2 == 0):
					print('Число четное')
				else:
					print('Число нечетное')
			elif (countInput == 6):
				score -= 8
				if (digit % 3 == 0):
					print('Число делится на 3')
				else:
					print('Число не делится на 3')
			elif (countInput == 5):
				score -= 4
				if (digit % 4 == 0):
					print('Число делится на 4')
				else:
					print('Число не делится на 4')
			elif (countInput > 2 and countInput < 5):
				score -= 2
				if (digit < x):
					print('Загаданное число МЕНЬШЕ вашего')
				else:
					print('Загаданное число БОЛЬШЕ вашего')
			score -=5
		countInput += 1

	print('-' * 30)
	if (x == digit):
		print('Победа! Поздравляем!')
		print(f'Заработано очков: {score}')
	else:
		print('Ой, у вас закончились очки. Вы проиграли :(')

	if (input('Enter - сыграть ещё, 0 - выход ') == '0'):
		playGame = False
	else:
		win = False

	if (score > maxScore):
		maxScore = score

print('-' * 30)
print('''Спасибо что сыграли в мою игру!
Возвращайтесь скорей! Буду ждать с нетерпением!
P.S. Вы хорошо держались :)''')