import unittest
from function import task_25

class FunctionTestCase(unittest.TestCase):
  def test_task_25_values(self):
    self.assertEqual(task_25(0), -7)
    self.assertEqual(task_25(2), 161)
    self.assertEqual(task_25(3.5), 5434.296875)
  
  def test_task_25_errors(self):
    self.assertRaises(TypeError, task_25, 'one')
    self.assertRaises(TypeError, task_25, 'x')
    
unittest.main()