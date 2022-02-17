class NonNumericError(Exception):
    pass

class InconsistentDataError(Exception):
    pass

s =[]

try:
    s = [int(i) for i in input('Введите катеты: ').split()]
except ValueError:
    raise NonNumericError('Вводить необходимо целые числа')
if len(s) %2 != 0:
    raise InconsistentDataError('Увы, введено нечетное количество катетов')

n = 0
for i in range(0, len(s)-1, 2):
    c = (s[i]**2 + s[i+1]**2)**0.5
    S = (s[i] * s[i+1]) / 2
    n += 1
    print(f'Треугольник {n} с катетами {s[i]} и {s[i+1]} имеет площадь {S} и гипотенузу {c}')
