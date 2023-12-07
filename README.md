# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Общее описание решения
В папке geometric_lib находятся 4 файла с функциями для вычисления площади и периметра геометрических фигур: круга, прямоугольника, квадрата и треугольника и папка docks, содержащая файл с документацпией.

### Circle.py
В файле находятся 2 функции Area(r) и Perimeter(r), вычисляющие площадь и периметр круга по формулам *S = πR²* и *P = 2πR* соответственно.

### Rectangle.py
В файле находятся 2 функции Area(r) и Perimeter(r), вычисляющие площадь и периметр прямоугольника по формулам *S = ab* и *P = 2a + 2b* соответственно.

### Square.py
В файле находятся 2 функции Area(r) и Perimeter(r), вычисляющие площадь и периметр квадрата по формулам *S = a²* и *P = 4a* соответственно.

### Triangle.py
В файле находятся 2 функции Area(r) и Perimeter(r), вычисляющие площадь и периметр треугольника по формулам *S = ah/2* и *P = a + b + c* соответственно.


# Описание каждой функции
## Circle.py  - файл для вычисления площади и периметра круга
### def area(r)
Принимает число *r* - радиус круга.
Возвращает произведение *πR²* - площадь круга с радиусом *r*.

**Примеры вызова функции :**

    Входные данные         Выходные данные

    area(1)                3.141592653589793

    area(3)                28.274333882308138

### def perimeter(r)
Принимает число *r* - радиус круга.
Возвращает произведение *2πR* - периметр круга с радиусом *r*.

**Примеры вызова функции :**

    Входные данные         Выходные данные

    perimeter(1)           6.283185307179586 

    perimeter(3)           18.84955592153876

## Rectangle.py - файл для вычисления площади и периметра прямоугольника
### def area(r)
Принимает числа *a* и *b* - длины сторон прямоугольника.
Возвращает произведение *ab* - площадь прямоугольника.

**Примеры вызова функции :**

    Входные данные           Выходные данные

    area(1, 2)               2

    area(3, 4)               12

### def perimeter(r)
Принимает числа *a* и *b* - длины сторон прямоугольника.
Возвращает произведение *2(a+b)* - периметр прямоугольника.

**Примеры вызова функции :**

    Входные данные           Выходные данные

    area(1, 2)               6

    area(5.5, 6)             23.0

## Square.py - файл для вычисления площади и периметра квадрата
### def area(r)
Принимает число *a* - длины сторон квадрата.
Возвращает *a²* - площадь квадрата.

**Примеры вызова функции :**

    Входные данные           Выходные данные

    area(2)                  4

    area(5)                  25

### def perimeter(r)
Принимает число *a* - длины сторон квадрата.
Возвращает *4a* - периметр квадрата.

**Примеры вызова функции :**

    Входные данные           Выходные данные

    area(2)                  8

    area(5)                  20


## Triangle.py - файл для вычисления площади и периметра треугольника
### def area(r)
Принимает числа *a*, *h* - длины основания треугольника и его высоты соответственно.
Возвращает *ah/2* - площадь треугольника.

**Примеры вызова функции :**

    Входные данные              Выходные данные

    area(3, 2)                  3.0

    area(4, 5)                  16.0

### def perimeter(r)
Принимает числa *a*, *b*, *c* - длины сторон треугольника.
Возвращает *a+b+c* - периметр треугольника.

**Примеры вызова функции :**

    Входные данные              Выходные данные

    perimeter(1, 2, 3)          6

    perimeter(5, 6, 7)          18
### История изменения проекта с хешами комитов (кроме последней записи)

### Коммит 7
Hash: **b29bd7875db7b6ab4fae50ce652c7346b1e3c1e0** 

Author:Sanchell1o <trollbabich1@mail.ru>

Date: Thu Oct 26 14:28:52 2023 +0300
  
    added files for testings


### Коммит 6
Hash: **0aca9cca28e306dabe1c5cf740a5bfa4e226ebda**

Author: Sanchell1o <trollbabich1@mail.ru>

Date:   Wed Oct 11 19:34:53 2023 +0300

    Added documentation for rectangle.py and square.py


### Коммит 5
Hash: **d183d7c48e71c7aa37be66a970ee6bad80ac1811**

Author: Sanchell1o <trollbabich1@mail.ru>

Date:   Wed Oct 11 19:33:56 2023 +0300

    Added documentation for circle.py and triangle.py


### Коммит 4
Hash: **0efe2f20abda9f9492a81e38c6b61dee3268e664**

Author: Sanchell1o <trollbabich1@mail.ru>

Date:   Tue Sep 26 18:30:55 2023 +0300

    Добавил triangle.py и исправил ошибку в вычислении периметра

### Коммит 3
Hash: **c149f5ebc8e110ca0c4807896d13f236b8855225**

Author: Sanchell1o <trollbabich1@mail.ru>

Date:   Tue Sep 26 18:28:17 2023 +0300

    Добавил rectangle.py

### Коммит 2
Hash: **d078c8d9ee6155f3cb0e577d28d337b791de28e2**

Author: smartiqa <info@smartiqa.ru>

Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

### Коммит 1
Hash: **8ba9aeb3cea847b63a91ac378a2a6db758682460**

Author: smartiqa <info@smartiqa.ru>

Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

# Tests  
Autotests success: 16/20 (80%)  
