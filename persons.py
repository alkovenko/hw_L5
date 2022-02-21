import collections

my_list = [{'name': 'Anna', 'age': 25, 'gender': 'female'},
{'name': 'Lena', 'age': 12, 'gender': 'female'},
{'name': 'Nastya', 'age': 33, 'gender': 'female'},
{'name': 'Angelina', 'age': 30, 'gender': 'female'},
{'name': 'Anna', 'age': 22, 'gender': 'female'},
{'name': 'Anna', 'age': 40, 'gender': 'female'},
{'name': 'Ira', 'age': 11, 'gender': 'female'},
{'name': 'Polina', 'age': 17, 'gender': 'female'},
{'name': 'Oksana', 'age': 18, 'gender': 'female'},
{'name': 'Anna', 'age': 8, 'gender': 'female'},
{'name': 'Yana', 'age': 43, 'gender': 'female'},
{'name': 'Kira', 'age': 18, 'gender': 'female'},
{'name': 'Nastya', 'age': 25, 'gender': 'female'},
{'name': 'Tamara', 'age': 31, 'gender': 'female'},
{'name': 'Rita', 'age': 39, 'gender': 'female'},
{'name': 'Sveta', 'age': 25, 'gender': 'female'},
{'name': 'Anna', 'age': 22, 'gender': 'female'},
{'name': 'Nastya', 'age': 28, 'gender': 'female'},
{'name': 'Lera', 'age': 19, 'gender': 'female'},
{'name': 'Sara', 'age': 10, 'gender': 'female'},
{'name': 'Alex', 'age': 44, 'gender': 'male'},
{'name': 'Dima', 'age': 33, 'gender': 'male'},
{'name': 'Fedor', 'age': 38, 'gender': 'male'},
{'name': 'Nikita', 'age': 32, 'gender': 'male'},
{'name': 'Alex', 'age': 25, 'gender': 'male'},
{'name': 'Foma', 'age': 7, 'gender': 'male'},
{'name': 'Evgeniy', 'age': 25, 'gender': 'male'},
{'name': 'Alex', 'age': 12, 'gender': 'male'},
{'name': 'Kiril', 'age': 27, 'gender': 'male'},
{'name': 'Mihail', 'age': 30, 'gender': 'male'}]

male = 0
female = 0
age_18 = 0
names = []
ages = []
most_names = collections.defaultdict(int)
male_35_F = []


for persons in my_list:
    if persons['gender'] == 'male':
        male += 1
    else:
        female += 1
    if persons['age'] >= 18:
        age_18 += 1
    if persons['name'] not in names:
        names.append(persons['name'])
    if persons['age'] not in ages:
        ages.append(persons['age'])
    most_names[persons['name']] += 1
    if persons['name'][0] == 'F' and persons['age'] > 35:
        male_35_F.append(persons['name'])

most_three = [(v, k) for k, v in most_names.items()]
most_three.sort()
most_three = most_three[-3:]
most_three = [i[1] for i in most_three]

ages.sort()
print(male, female, age_18, names, ages, most_three, male_35_F, sep='\n')
