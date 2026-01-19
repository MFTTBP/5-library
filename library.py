""""
this is ,y library project
"""
library: dict[str, str] = {"Кладбище домашних животных": "Steaven King", "Долгая дорога" : "Steaven King", "Долгие ночи" : "А.А. Айдамиров"}

authors = set(library.values())

print(list(library.keys()))
print(list(authors))
