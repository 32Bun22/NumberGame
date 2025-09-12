from faker import Faker
import random
fake = Faker()
a = random.randint(10, 10)
b = int(input("Введите ваше число: "))
if (b == a):
    print("Вы угадали число!")
else:
    print("Вы не угадали число! Правильное число:", a, ".")
for _ in range(10):
    print(fake.name())
print(fake.address())

nikita = ("никита")

# TODO: Добавить проверку на пустой ввод
