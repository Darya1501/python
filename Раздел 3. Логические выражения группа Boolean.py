print("Раздел 3. Логические выражения: группа Boolean")

print("Задача 10. Даны два числа А и Б. Проверить истинность высказывания \"Ровно одно из чисел нечетное\"")
print("Решение: ")
a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = a + b
bool = c%2 == 1
print(bool)

print("____________")

print("Задача 33. Даны целые числа a, b, c. Проверить истинность высказывания \"Существует треугольник со сторонами a, b, c \"")
print("Решение: ")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
x1 = a + b - c
x2 = a + c - b
x3 = b + c - a
bool1 = x1 > 0
bool2 = x2 > 0
bool3 = x3 > 0
bool = bool1 and bool2 and bool3
print(bool)
