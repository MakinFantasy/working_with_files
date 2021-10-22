from pprint import pprint
import os


def task_1_cookbook():
    path = os.path.join(os.getcwd(), 'recipes.txt')

    with open(path, encoding="utf-8") as file:
        result = {}
        for dish in file:
            dish_name = dish.strip()
            counter = int(file.readline().strip())
            temp_data = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_data.append(
                    {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()}
                )
            result[dish_name] = temp_data
            file.readline()
        return result


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    q = {}
    for dish in  dishes:
        if dish in q.keys():
            q[dish] += 1
        else:
            q[dish] = 1
    for dish_name, value in q.items():
        for ingredient_dict in cook_book[dish_name]:
            if not (ingredient_dict["ingredient_name"] in res.keys()):
                temp_dict = {
                        "measure": ingredient_dict["measure"],
                        "quantity": ingredient_dict["quantity"] * value * person_count
                    }
                res[ingredient_dict["ingredient_name"]] = temp_dict
            else:
                res[ingredient_dict["ingredient_name"]]["quantity"] += ingredient_dict["quantity"] \
                                                                       * value \
                                                                       * person_count
    return res


def sorted_files(list_file):
    result_task3 = {}
    for f_name in list_file:
        path = os.path.join(os.getcwd(), 'sorted', f_name)
        new_name = f_name
        with open(path, encoding='utf-8') as f_name:
            counter = 0
            for _ in f_name:
                counter += 1
            result_task3[new_name] = counter
        result_task3 =  dict(sorted(result_task3.items(), key=lambda x:x[1]))
    path1 = os.path.join(os.getcwd(), '', "result.txt")
    with open(path1, 'w', encoding="utf-8") as new_file:
        for key, value in result_task3.items():
            path = os.path.join(os.getcwd(), 'sorted', key)
            new_file.write(key + "\n")
            new_file.write(str(value)+"\n")
            with open(path, encoding="utf-8") as txt:
                new_file.write(txt.read() + '\n')


cook_book = task_1_cookbook()
list_shop = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(cook_book)
print()
pprint(list_shop)
files_list = ['1.txt', '2.txt', '3.txt']
sorted_files(files_list)
