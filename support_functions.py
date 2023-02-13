
def correct_number(n):
   try:
      while int(n) <= 0 or int(n) > 3:
         return False
      return True
   except ValueError:
      return False
   return n


def choose_option(request, ok):
  option = input('{}'.format(request))
  while ok(option) == False:
      print('No ha introducido una opción válida')
      option = input('Introdúzcalo de nuevo')

  return option
