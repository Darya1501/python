print("Раздел 2. Целые числа группа Integer")

print("Задача 16. Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков.")
print("Решение: ")
x = int(input("Введите число: "))
a = x // 100
b = (x - a*100) // 10
c = x - a*100 - b*10
d = str(b) + str(a) + str(c)
print("Новое число", d)

print("___________")


print("Задача 23. С начала суток прошло N секунд (N - целое). Найти количество минут, прошедших с начала последнего часа.")
print("Решение: ")
x = int(input("Введите количество секунд: "))
a = x // 60 # минуты
b = a // 60 # часы
c = a - b*60
d = str(b) + ":" + str(c)
print("С последнего часа прошло", c, "минут, время: ", d)
