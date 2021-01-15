#
number = int(input('Введите чило: '))
max_num = 0
while number != 0:
    num = number % 10
    number = number // 10
    if max_num < num:
        max_num = num
print(f"Ответ: {max_num}")