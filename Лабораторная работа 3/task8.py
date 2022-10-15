money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

first_month = (money_capital - spend) + salary
while first_month > 0:
    spend = spend * (increase + 1)
    first_month = (first_month - spend) + salary
    month += 1


print(month)
