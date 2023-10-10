# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44 * 1024 * 1024
volume_book = 50 * 100 * 24 * 4
quantity_books = volume_disk / volume_book
print("Количество книг, помещающихся на дискету:", int(round(quantity_books,0)))
