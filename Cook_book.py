def cook_book_dict(dishs, quantity_ingredients, ing_list):  # Создаем кулинарную книгу
    cook_list = []
    cook_book_ = {}
    for i in quantity_ingredients:
        y = ing_list[:i:]
        del ing_list[:i:]
        cook_list.append(y)
        cook_book_ = dict(zip(dishs, cook_list))
    return cook_book_


def main_f(file):  # Обрабатываем файл
    ing_list = []
    dishs = []
    quantity_ingredients = []
    _ = 1
    while _ != '':
        dish = file.readline().strip()
        ingredients = int(file.readline().strip())
        dishs.append(dish)
        quantity_ingredients.append(ingredients)
        for ingredient in range(ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split('|')
            ing_dict = ({'ingredient_name': ingredient_name.strip(),
                         'quantity': int(quantity), 'measure': measure.strip()})
            ing_list.append(ing_dict)
        _ = f.readline()
    return cook_book_dict(dishs, quantity_ingredients, ing_list)


def get_shop_list_by_dishes(dishes, person_count):  # Принимаем заказ
    dict_order = {}
    if person_count:
        for d_name in dishes:
            for ingredients in cook_book[d_name]:
                name = ingredients['ingredient_name']
                # print(name)
                quantity = ingredients['quantity']
                measure = ingredients['measure']
                dict_order.setdefault(name, {}).setdefault('measure', measure)
                dict_order[name]['quantity'] = (dict_order.setdefault(name, {})
                                                .setdefault('quantity', 0)
                                                + int(quantity) * int(person_count))

        return 'Ингредиенты к заказу', dict_order
    return 'Заказ отменен'


with open('Recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = main_f(f)

print(cook_book)

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
