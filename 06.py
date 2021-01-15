#
days = 1
first_jogging = float(input("Результат в первый день: "))
last_jogging = float(input("Нужный результат: "))
while last_jogging > first_jogging:
    first_jogging += first_jogging * 0.1
    days += 1
print(f'Нужный результат будет достигнут через {days} дней')