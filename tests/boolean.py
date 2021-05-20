# Задача 10. Даны два числа А и Б. Проверить истинность высказывания "Ровно одно из чисел нечетное"

def task_10(a, b):
  if type(a) not in [int, float] or type(b) not in [int, float]:
    raise TypeError('Введите два числа!')
  c = a + b
  bool = c%2 == 1
  return bool