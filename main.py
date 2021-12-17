print('Сумма чисел')

# Функция summa_n принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15


def summa_of_numbers(number_last):
    summa = 0
    for i in range(number_last + 1):
        summa += i
    return summa


number = int(input('Введите число: '))

print('Я знаю, что сумма чисел от 1 до', number, 'равна', summa_of_numbers(number))
