print("Раздел 4. Условный оператор: группа if")

print("Задача 26. Для данного вещественного х найти значение функции:")
print("если (x <= 0): f = -x / если (0 < x < 2): f = x^2 / если (x >= 2): f = 4")
print("Решение: ")
x = float(input("Введите x: "))
if x <= 0 :
    y = -x
elif x < 2:
    y = x**2
else:
    y = 4
print("Ответ: ", y)

print("____________")


print("Задача 30. Дано целое число от 1 до 999, вывести строку описание этого числа")
print("Решение: ")
a = int(input("Введите число от 1 до 999: "))
bool = True

if a%2 == 1:
    str1 = "Нечетное "
else:
    str1 = "Четное "

if 1 <= a <= 9:
    str2 = "однозначное "
elif 10 <= a <= 99:
    str2 = "двузначное "
elif 100 <= a <= 999:
    str2 = "трехзначное "
else:
    bool = False

if bool:
    str = str1 + str2 + "число"
else:
    str = "Нужно было ввести число от 1 до 999"
    
print(str)
