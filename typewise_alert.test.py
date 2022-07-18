import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    cooling_type_object = typewise_alert.cooling_type(100, 50, 20)
    self.assertTrue(cooling_type_object.infer_breach == 'TOO_HIGH')


if __name__ == '__main__':
  unittest.main()
