class NonNumericError(Exception):
    pass

class InconsistentDataError(Exception):
    pass

a, b = [], []

try:
    a = [int(i) for i in input('Введите первые катеты а: ').split()]
    b = [int(i) for i in input('Введите вторые катеты b: ').split()]
except ValueError:
    raise NonNumericError('Вводить необходимо целые числа')

if len(a) != len(b) or len(a) %2 != 0:
    raise InconsistentDataError('Увы, введено разное количество катетов, либо их нечетное количество')

for i in range(len(a)):
    c = (a[i]**2 + b[i]**2)**0.5
    S = (a[i] * b[i]) / 2
    print(f'Треугольник {i+1} с катетами {a[i]} и {b[i]} имеет площадь {S} и гипотенузу {c}')
