import unittest
from boolean import task_10

class NumberTestCase(unittest.TestCase):
  def test_task_10_values(self):
    self.assertEqual(task_10(1, 1), False)
    self.assertEqual(task_10(1, 2), True)
    self.assertEqual(task_10(2, 2), False)
  
  def test_task_10_errors(self):
    self.assertRaises(TypeError, task_10, 'one')
    self.assertRaises(TypeError, task_10, 'x')
    
unittest.main()