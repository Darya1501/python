# Задача 16. Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков.

def task_16(x):
  if type(x) not in [int]:
    raise TypeError('Введите целое число!')
  if x < 100 or x > 999:
    raise ValueError('Необходимо трёхзначное число')
  a = x // 100
  b = (x - a*100) // 10
  c = x - a*100 - b*10
  d = str(b) + str(a) + str(c)
  return int(d)