def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    n = index
    if n:
        list_.pop(n)
    elif n==0:
        list_.pop(0)
    else:
        list_.pop(-1)

    return list_

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
