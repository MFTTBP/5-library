""""
this is ,y library project
"""
import sys


books: dict[str, str] = {
    "Кладбище домашних животных": "Steaven King",
    "Долгая дорога": "Steaven King",
    "Долгие ночи": "А.А. Айдамиров",
    "Зелемхан": "А.А. Айдамиров"}
authors = set(books.values())

if len(sys.argv) < 2:
    print("Укажите action: filter или sort")
    sys.exit(1)

action = sys.argv[1]

if action == "filter":
    if len(sys.argv) < 3:
        print("Укажите книгу")
        sys.exit(1)
    books_to_find = sys.argv[2]
    filtred_books = filter(lambda x: x == books_to_find, books.keys())
    result = list(map(lambda b: f"{b} — {books[b]}", filtred_books))
    print(result)
elif action == "sort":
    if len(sys.argv) < 3:
        print("Укажите критерий books или author")
        sys.exit(1)
    sort_by = sys.argv[2].lower()
    mapped_books = list(map(lambda b: f"{b} — {books[b]}", books.keys()))
    if sort_by == "book":
        sort_books = sorted(mapped_books, key=lambda x: x.split("-")[0])
    elif sort_by == "author":
        sort_books = sorted(mapped_books, key=lambda x: x.split("-")[1])
    else:
        print("Неверный критерий сортировки: используйте book или author")
        sys.exit(1)
    print(sort_books)
else:
    print("Неверный action. Используйте filter или sort")
