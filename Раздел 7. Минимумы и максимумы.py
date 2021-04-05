print("Раздел 7. Минимумы и максимумы")

print("Задача 6. Дано целое число N и набор из N целых чисел. Найти номера первого минимального и последнего максимального элемента из данного набора и вывести их в указанном порядке.")
print("Решение: ")
s = int(input("Введите размер массива: "))
a = [0]*s

print("Введите элементы массива: ")
for i in range(0, s):
    a[i] = int(input())

minin = 0
maxin = 0

for f in range(0, s):
    if a[f] < a[minin]:
        minin = f
for b in range(0, s):
    if a[b] >= a[maxin]:
        maxin = b
    
print("Порядковый номер первого минимального:", minin+1, ", порядковый номер последнего максимального:", maxin+1)


print("____________")

print("Задача 17. Дано целое число N и набор из N целых чисел. Найти количество элементов, расположенных после последнего максимального элемента.")
print("Решение: ")
s = int(input("Введите размер массива: "))
a = [0]*s

print("Введите элементы массива: ")
for i in range(0, s):
    a[i] = int(input())

maxin = 0

for b in range(0, s):
    if a[b] >= a[maxin]:
        maxin = b

s = s - maxin - 1
    
print("Элементов после последнего максимального:", s)
