import random
a = random.randint(10, 15)
b = int(input("Введите ваше число: "))
if (b == a):
    print("Вы угадали число!")
else:
    print("Вы не угадали число! Правильное число:", a)