cook_book = {}
with open ('cook_book.txt', 'rt', encoding='utf8') as content:
    for line in content:
        name_dish = line.rstrip()
        ingredients = []
        number = content.readline()
        for num in range(int(number)):
            num_ = content.readline()
            ingredient_name, quantity, measure = num_.split(' | ') 
            ingredients.append({'ingredient_name': ingredient_name,
                                        'quantity': quantity,
                                        'measure': measure})
        blackline = content.readline()
        cook_book.update({name_dish: ingredients})
 


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for ind in dishes:
        if ind in cook_book.keys():
            for i in cook_book[ind]:
                pers_quantity = int(i['quantity']) * person_count
                shop_list.update({i['ingredient_name']: {'measure':i['measure'], 'quantity': pers_quantity}})
    print(shop_list)
   
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)