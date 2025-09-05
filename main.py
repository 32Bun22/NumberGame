import random
a = random.randint(10, 10)
c = random.randint(10, 10)
b = int(input("Введите ваше число: "))
d = int(input("Введите ваше число: "))
if (b == a and c == d):
    print("Вы угадали числа!")
elif ((b == a and c != d) or (b != a and c == d)):
    print("Вы угадали одно из чисел.")
else:
    print("Вы не угадали числа! Правильные числа:", a," и ", c)