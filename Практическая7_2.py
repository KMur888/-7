# Создать любой список. Определить, есть ли в списке повтор элементы, если да, то вывести на экран это значение.
my_list = [1, 1, 3, 2, 8, 5, 3]
repeated = []
for i in my_list:
    if my_list.count(i) > 1 and i not in repeated:
        repeated.append(i)
print("Повторяющиеся элементы:", repeated)