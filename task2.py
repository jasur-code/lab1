# TODO Найдите количество книг, которое можно разместить на дискете


# Размер дискеты в байтах
skette_size = 1.44 * 1024 * 1024
count_of_books = int(skette_size // (4 * 25 * 50 * 100))

print("Количество книг, помещающихся на дискету:", count_of_books)