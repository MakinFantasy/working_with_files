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



