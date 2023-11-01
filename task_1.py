# TODO Напишите функцию для поиска индекса товара
def find_items(item_list, item_to_find):
    if item_to_find in item_list:
        return item_list.index(item_to_find)
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_items_list = ['банан', 'груша', 'персик']

for find_item in find_items_list:
    index_item = find_items(items_list, find_item)  # Вызывается функция для поиска индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")