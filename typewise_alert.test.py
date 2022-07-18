import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(100, 50, 20) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
