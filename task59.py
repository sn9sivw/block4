
number = input("Введите четырехзначное число: ")


if '4' in number:
    print("Да, в числе есть цифра 4")
else:
    print("Нет, в числе нет цифры 4")

b = input("Введите цифру для поиска: ")


if b in number:
    print(f"Да, в числе есть цифра {b}")
else:
    print(f"Нет, в числе нет цифры {b}")
