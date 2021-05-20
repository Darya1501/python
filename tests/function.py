# Задача 25. Найти значение функции y=3*x^6-6*x^2-7 при заданном значении х.

def task_25(x):
  if type(x) not in [int, float]:
    raise TypeError('Введите число!')
  y = 3 * x**6 - 6 * x**2 - 7
  return y