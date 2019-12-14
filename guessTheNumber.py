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

digit = random.randint(lowDigit, highDigit)
print('Копьютер загадал число, попробуйте отгадать!')
print(f'Загаданное число: {digit}')

x = ''
while (not x.isdigit()):
	x = input(f'Введите число от {lowDigit} до {highDigit}: ')
	if (not x.isdigit()):
		print('.' * 27 + 'Введите, пожалуйста, число.')

x = int(x)

if (x == digit):
	print('Победа! Поздравляем!')