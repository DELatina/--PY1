money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

x = money_capital - spend
while x > 0:
    y = x + salary
    spend = spend * (1 + increase)
    x = y - spend
    month += 1


print(month)
