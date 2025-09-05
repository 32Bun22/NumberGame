import random
a = random.randint(-225, 225)
b = int(input("Введите ваше число: "))
if (b == a):
    print("Вы угадали число!")
else:
    print("Вы не угадали число! Правильное число:", a)