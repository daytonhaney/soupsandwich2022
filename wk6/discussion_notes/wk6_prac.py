def find_my_elements(list_1, list_2):
    return [list_1[i] for i in list_2]


list_1 = [10, 20, 30, 40, 50, 60, 70, 80]
list_2 = [0, 2, 4]

print(find_my_elements(list_1, list_2))


def another_approach(list_1, list_2):
    return list(map(list_1.__getitem__, list_2))


list_1 = [10, 20, 30, 40, 50, 60, 70, 80]
list_2 = [0, 2, 4]

print(another_approach(list_1, list_2))

list_3 = ['cat', 'bat', 'mat', 'cat', 'dog', ]

print(list_3.index('mat'))


x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
