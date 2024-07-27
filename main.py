# Задание №1
with open('recipes.txt', 'r', encoding='utf-8') as file:
    book_cook = {}
    for line in file:
        dishes = line.strip()
        list_ingredients = []
        for _ in range(int(file.readline().strip())):
            ingridient = file.readline().strip().split('|')
            list_ingredients.append({'ingredient_name': ingridient[0], 'quantity': int(ingridient[1]),
                                     'measure': ingridient[2]})
        book_cook[dishes] = list_ingredients
        file.readline()

# Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    food_basket = {}
    for dish in dishes:
        for ingredient in book_cook[dish]:
            if ingredient['ingredient_name'] not in food_basket:
                food_basket[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                              'quantity': ingredient['quantity'] * person_count}
            else:
                food_basket[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return food_basket


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание №3

with open('1.txt', 'r', encoding='utf-8') as file1, open('2.txt', 'r', encoding='utf-8') as file2, \
        open('3.txt', 'r', encoding='utf-8') as file3, open('result.txt', 'w', encoding='utf-8') as result:
    files_dict = {}
    for file in [file1, file2, file3]:
        files_dict[file.name] = file.readlines()

    for name_file in sorted(files_dict, key=lambda x: len(files_dict[x])):
        result.write(name_file + '\n')
        result.write(str(len(files_dict[name_file])) + '\n')
        result.write(''.join(files_dict[name_file]))

