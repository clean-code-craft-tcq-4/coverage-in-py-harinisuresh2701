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
    
def send_to_controller(breachType,print_message_on_console,header):
  controller_message = format_controller_message(header, breachType)
  print_message_on_console(controller_message)
  return controller_message

def send_to_email(breachType, print_message_on_console,recepient):
  recepient_message = format_recepient(recepient)
  print_message_on_console(recepient_message)
  if breachType == 'TOO_LOW':    
    breach_message_on_console = 'Hi, the temperature is too low'
  elif breachType == 'TOO_HIGH':
    breach_message_on_console = 'Hi, the temperature is too high'
  print_message_on_console(breach_message_on_console)
  return breachType,breach_message_on_console

def check_and_alert(coolingType, temperatureInC, classify_temperature_breach, send_to_controller_or_email,print_message_on_console,recepient_or_header):
  breachType =\
    classify_temperature_breach(coolingType, temperatureInC)
  send_to_controller_or_email(breachType,print_message_on_console,recepient_or_header)
