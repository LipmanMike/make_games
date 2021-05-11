import random

guesses_taken = 0

print('Привет! Как тебя зовут?')

username = input()

number = random.randint(1, 20)

print('Итак, ' + username + ', я загадываю число от 1 до 20.')

for guesses_taken in range(6):
    print('Попробуй угадать число: ')

    guess = int(input())

    if guess < number:
        print('загаданное число больше')
    elif guess > number:
        print('загаданное число меньше')
    else:
        break

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print('Отлично, ' + username + '! ты справился за ' + guesses_taken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы, я загадал ' + number + '.')


