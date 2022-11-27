salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
i = 1
while i <= months:
    money_capital += spend - salary
    spend = spend + (spend * increase)
    i += 1
print(round(money_capital))
