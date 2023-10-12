# TODO Найдите количество книг, которое можно разместить на дискете



# Заданные параметры
page_lines = 50
characters_per_line = 25
bytes_per_character = 4
pages_per_book = 100
diskette_size_bytes = 1.44 * 1024 * 1024  # 1.44 Мб в байтах

# Рассчитываем размер одной страницы
bytes_per_page = page_lines * characters_per_line * bytes_per_character

# Рассчитываем размер одной книги
bytes_per_book = pages_per_book * bytes_per_page

# Рассчитываем количество книг, которое помещается на дискету
books_on_diskette = diskette_size_bytes // bytes_per_book

# Выводим результат на экран
print("Количество книг, помещающихся на дискету:", int(books_on_diskette))
