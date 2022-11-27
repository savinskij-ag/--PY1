list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
k = 0
i1 = i2 = 0
for i in range(len(list_numbers)):
    if list_numbers[i] >= list_numbers[i1]:
        i1 = i
    if list_numbers[i] >= list_numbers[i2]:
        i2 = i

[list_numbers[len(list_numbers)-1], list_numbers[i2]] = [list_numbers[i2], list_numbers[len(list_numbers)-1]]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
