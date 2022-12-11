import random

def get_unique_list_numbers() -> list[int]:
    unique = []
    while len(unique) != 15:
        number = random.randint(-10, 10)
        if number not in unique:
            unique.append(number)
    return unique

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
