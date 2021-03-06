from math import(sqrt)
sqr = input('Введите название фигуры, которое описывает вид комнаты (прямоугольник),(круг),(треугольник): ')
if sqr == 'прямоугольник':
    a = int(input('длинна равна: '))
    b = int(input('ширина равна: '))
    print(float(a*b))
elif sqr == 'круг':
    r = int(input('радиус равен: '))
    print(3.14 * (r**2))
elif sqr == 'треугольник':
    a = int(input('первая сторона: '))
    b = int(input('вторая сторона: '))
    c = int(input('третья сторона: '))
    per = (a + b + c) / 2
    ger = per * ((per - a) * (per - b) * (per - c))
    ger = sqrt(ger)
    print(float(ger))

'''Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и
круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и
соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14. Формат ввода, который используют Малевийцы:
треугольник
a
b
c
где a, b и c — длины сторон треугольника
прямоугольник
a
b
где a и b — длины сторон прямоугольника
круг
r
где r — радиус окружности

'''