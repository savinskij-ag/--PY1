from random import randint
def get_unique_list_numbers() -> list[int]:
    unique = []
    for number in list_unique_numbers:
        if number in unique:
            continue
        else:
            if len(unique) < 15:
                unique.append(number)
                list_unique_numbers[number]==list_unique_numbers[number - 1]
            else: break
    return unique

# TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = []
for x in range(-12, 10):
    list_unique_numbers.append(randint(-10, 10))

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
