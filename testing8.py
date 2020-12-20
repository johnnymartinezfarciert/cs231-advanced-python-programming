#  Use unittest.TestCase methods to confirm that the addition and subtraction
# of date and timedelta objects produce correct results
import unittest
from datetime import datetime

class subtractTime():
   def subtractTime(a,b):
       return  datetime.strptime(a, '%H:%M:%S') - datetime.strptime(b, '%H:%M:%S')

class test_subtractTime(unittest.TestCase):
    def test_subtractTime(self):
        result = subtractTime.subtractTime('23:59:59','00:00:01')
        self.assertEquals(result, datetime.strptime('23:59:58', '%H:%M:%S'))
    unittest.main(verbosity=2)
