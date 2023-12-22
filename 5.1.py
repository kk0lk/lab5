"""

Задача №1

Напишіть функцію для сортування рядка в порядку, протилежному алфавітному,
без врахування регістру літер.
Вхідні дані:
Ruby
Вихідні дані:
yuRb

Виконала: Гриб Наталія Григорівна, 31І група

"""

def sort_reversed_case_insensitive(n):

  # Перетворюємо рядок в список символів.
  characters = list(n)

  # Сортуємо список символів в порядку, протилежному алфавітному.
  return "".join(sorted(n.lower(), reverse=True))

n = input("Введіть слово: ")

sorted_n = sort_reversed_case_insensitive(n)

print(sorted_n)
