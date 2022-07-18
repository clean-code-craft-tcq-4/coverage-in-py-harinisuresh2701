import unittest
import typewise_alert

def print_message_on_console_stub(message):
    print(message)  
    
class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    cooling_type_object = typewise_alert.cooling_type(100, 50, 20)
    self.assertTrue(cooling_type_object.breach_type == 'TOO_HIGH')
    
    cooling_type_object = typewise_alert.cooling_type(5, 50, 20)
    self.assertTrue(cooling_type_object.breach_type == 'TOO_LOW')
        
    cooling_type_object = typewise_alert.cooling_type(30, 50, 20)
    self.assertTrue(cooling_type_object.breach_type == 'NORMAL')
    
  def test_classify_temperature_breach(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',50) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',-5) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 100) == 'TOO_HIGH')
  
  def test_format_controller_message(self):
        self.assertTrue(typewise_alert.format_controller_message(0xfeed, 'TOO_LOW') == "0xfeed, TOO_LOW")

  def test_format_recepient(self):
    self.assertTrue(typewise_alert.format_recepient('test@trial.com') == "To: test@trial.com")
    
  def test_send_to_controller(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_LOW',print_message_on_console_stub) == "0xfeed, TOO_LOW")
  
  def test_send_to_email(self):
    recepient_message,breach_message_on_console = typewise_alert.send_to_email('TOO_HIGH', print_message_on_console_stub)
    self.assertTrue(recepient_message == "To: a.b@c.com")
    self.assertTrue(breach_message_on_console == "Hi, the temperature is too high")
    
    recepient_message,breach_message_on_console = typewise_alert.send_to_email('TOO_LOW', print_message_on_console_stub)
    self.assertTrue(breach_message_on_console == "Hi, the temperature is too low")
    
  def test_check_and_alert(self):
    breachType, controller_message = typewise_alert.check_and_alert('TO_CONTROLLER', "PASSIVE_COOLING", 45)
    self.assertTrue(breachType == "TOO_HIGH")
    self.assertTrue(controller_message == "0xfeed, TOO_HIGH")
    
    breachType, controller_message = typewise_alert.check_and_alert('TO_EMAIL', "PASSIVE_COOLING", -5)    
    self.assertTrue(breachType == "TOO_LOW")
    self.assertTrue(controller_message[0] == "To: a.b@c.com")
    self.assertTrue(controller_message[1] == "Hi, the temperature is too low")
    
if __name__ == '__main__':
  unittest.main()
