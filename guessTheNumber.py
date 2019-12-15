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

# -------------------------------- Главный цикл
while (playGame):  
	digit = random.randint(lowDigit, highDigit)	# Загадываем число
	# print(f'Загаданное число: {digit}')  Вывод загаданного числа
	print('-' * 30)
	countInput = 0
	score = startScore
	print('Я загадал число, попробуйте отгадать!')

# -------------------------------- Внутренний цикл
	while (not win and score > 0):		
		print('-' * 45)
		print(f'Заработано очков: {score}')
		print(f'Рекорд: {maxScore}')

# -------------------------------- Контроль ввода числа
		x = ''
		diapason = False
		xIsDigit = True	     			# Сбрасываем для условия в while
		while (xIsDigit and not diapason):
			x = input(f'Введите число от {lowDigit} до {highDigit}: ')
			if (not x.isdigit()):
				xIsDigit = True
				print('.' * 17 + 'Введите, пожалуйста, число.')
			else:
				x = int(x)
				diapason = (x >= lowDigit and x <= highDigit)
				if (not diapason):
					print('.' * 17 + f'Число от {lowDigit} до {highDigit}')

# -------------------------------- Подсказки
		if (x == digit):				# Сбрасываем win для выхода при победе
			win = True 		
		else:							# Иначе активируем подсказки
			length = abs(x - digit)
			if (length < 3):			# Удаленность от числа
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

			if (countInput == 7):		# Увеличение числа ходов
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
# -------------------------------- Конец внутреннего цикла

	print('-' * 45)
	if (x == digit):
		print('Победа! Поздравляю!')
		print(f'Заработано очков: {score}')
	else:
		print('Ой, у вас закончились очки. Вы проиграли :(')

	if (input('Enter - сыграть ещё, 0 - выход ') == '0'):
		playGame = False
	else:
		win = False

	if (score > maxScore):
		maxScore = score
# -------------------------------- Конец главного цикла

print('-' * 45)
print(f'Лучший результат: {maxScore}')
print('''Спасибо что сыграли в мою игру!
Возвращайтесь скорей! Буду ждать с нетерпением!
P.S. Вы хорошо держались :)''')
