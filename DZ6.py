import random

checklist = [
          "Дария", "Салават", "Марат", "Эльдар", "Владимир", "Булат",
          "Мансур", "Aлим", "Фарида", "Роман", "Ирина", "Рустам",
          "Тимур", "Илья", "Аделя", "Булат", "Евгений", "Лия",
          "Ксения", "Никита", "Андрей", "Расим", "Аяз", "Ильдус",
          "Нафис", "Александр", "Ильмир", "Павел", "Тимур", "Виктория",
          "Дария", "Салават", "Марат", "Эльдар", "Владимир", "Булат"
          ]
sampling = random.choices( checklist, k = 20)
dividing2 = random.choices( checklist, k = 20)
dividing3 = random.choices( checklist, k = 20)
a = set(dividing3)
b = set(dividing2)
c = set(sampling)
i = a & b & c
print("Выборка с методом choices " , sampling)
print("Выборка с методом choices " , dividing2)
print("Выборка с методом choices " , dividing3)
print(i)
a.update(b,c)
a.difference_update(i)
print(a)
