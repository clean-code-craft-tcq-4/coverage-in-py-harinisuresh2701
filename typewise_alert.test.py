import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    cooling_type_object = typewise_alert.cooling_type()
    self.assertTrue(cooling_type_object.infer_breach(100, 50, 20) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
