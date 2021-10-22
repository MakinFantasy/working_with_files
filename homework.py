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



