class cooling_type:
    breach_type = 'Default'
    def __init__(self,val,ul,ll):
        self.infer_breach(val,ul,ll)
    def infer_breach(self, value, upperLimit, lowerLimit):
      if value < lowerLimit:
        self.breach_type = 'TOO_LOW'
      elif value > upperLimit:
        self.breach_type = 'TOO_HIGH'
      else:
        self.breach_type = 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
    if coolingType == 'PASSIVE_COOLING':
        return(cooling_type(temperatureInC,35,0).breach_type)
    elif coolingType == 'HI_ACTIVE_COOLING':
        return(cooling_type(temperatureInC,45,0).breach_type)
    else:    
       return(cooling_type(temperatureInC,40,0).breach_type)
   
def format_controller_message(header, breachType):
    formatted_string = (f'{hex(header)}, {breachType}')
    return formatted_string
  
def format_recepient(recepient):
    formatted_string = (f'To: {recepient}')
    return formatted_string
    
def print_message_on_console(message):
    print(message)    
    
def send_to_controller(breachType,print_message_on_console):
  header = 0xfeed
  controller_message = format_controller_message(header, breachType)
  print_message_on_console(controller_message)
  return controller_message
    
def send_to_email(breachType, print_message_on_console):
  recepient = "a.b@c.com"
  recepient_message = format_recepient(recepient)
  print_message_on_console(recepient_message)
  if breachType == 'TOO_LOW':    
    breach_message_on_console = 'Hi, the temperature is too low'
  elif breachType == 'TOO_HIGH':
    breach_message_on_console = 'Hi, the temperature is too high'
  else:
    pass
  print_message_on_console(breach_message_on_console)
  return recepient_message,breach_message_on_console
     
def check_and_alert(alertTarget, coolingType, temperatureInC):
  breachType =\
    classify_temperature_breach(coolingType, temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    controller_message = send_to_controller(breachType,print_message_on_console)
  elif alertTarget == 'TO_EMAIL':
    controller_message = send_to_email(breachType, print_message_on_console)
  return breachType, controller_message
