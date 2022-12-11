def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = 25
n = 8
number = int(number)
length = int(n)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
print(get_random_password())

