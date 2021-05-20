import unittest
from number import task_16

class NumberTestCase(unittest.TestCase):
  def test_task_16_values(self):
    self.assertEqual(task_16(123), 213)
    self.assertEqual(task_16(222), 222)
  
  def test_task_16_errors(self):
    self.assertRaises(TypeError, task_16, 'one')
    self.assertRaises(TypeError, task_16, 'x')
    self.assertRaises(TypeError, task_16, 111.23)
    self.assertRaises(ValueError, task_16, 11)
    self.assertRaises(ValueError, task_16, 1111)
    
unittest.main()