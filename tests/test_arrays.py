import unittest
from arrays import task_53

class NumberTestCase(unittest.TestCase):
  def test_task_53_values(self):
    self.assertEqual(task_53([1, 2, 3, 4], [4, 3, 2, 1]), [4, 3, 3, 4])
    self.assertEqual(task_53([1, 2, 3, 4], [1, 2, 3, 4]), [1, 2, 3, 4])
    self.assertEqual(task_53([1, -2, -3, 4], [4, 3, 2, 1]), [4, 3, 2, 4])
  
  def test_task_53_errors(self):
    self.assertRaises(ValueError, task_53, [4, 3, 3, 4], [4, 3])
    
unittest.main()