revenue = float(input("Ваш доход: "))
costs = float(input("Ваши расходы: "))
profit = revenue - costs
if profit > 0:
    print(f'Рентабельность {profit / costs * 100} %')
    num_workers = int(input("Введите количество сотрудников: "))
    print(f'Прибыль на одного работника {profit / num_workers * 100} %')
elif profit < 0:
    print(f'Вы работаете в убыток {profit / costs * 100} %')
else:
    print(f'Ваша прибыль равна нулю.')