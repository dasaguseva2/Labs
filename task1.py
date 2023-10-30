def find_items(item_list, item_to_find):
    for index, item in enumerate(item_list):
        if item == item_to_find:
            return index
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_items_list = ['банан', 'груша', 'персик']

for find_item in find_items_list:
    index_item = find_items(items_list, find_item)  # Вызывается функция для поиска индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")