import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    cooling_type_object = typewise_alert.cooling_type(100, 50, 20)
    self.assertTrue(cooling_type_object.breach_type == 'TOO_HIGH')
    
    cooling_type_object = typewise_alert.cooling_type(5, 50, 20)
    self.assertTrue(cooling_type_object.breach_type == 'TOO_LOW')
        
    cooling_type_object = typewise_alert.cooling_type(30, 50, 20)
    self.assertTrue(cooling_type_object.breach_type == 'NORMAL')
    
  def test_classify_temperature_breach(self):
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',50) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-5) == 'TOO_LOW')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING', 100) == 'TOO_HIGH')

if __name__ == '__main__':
  unittest.main()
