# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не
# закончится список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0  # перемнная индекса списка
while number < len(my_list):
    if my_list[number] > 0:
        print(my_list[number])
        number += 1
    if my_list[number] == 0:
        number += 1
    continue
    if my_list[number] < 0:
        break



