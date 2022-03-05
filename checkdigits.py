"""
Name: Merathy Romain
Date: December 14, 2021
Description: Write a program that is able to determine whether a 12 digit UPC code or a 10 digit ISBN code is valid or not. Create a checkdigits module that will hold three functions named get_digit, is_UPC12 and is_ISBN10. The main file should hold the main function and the menu function. The checkdigits module should be imported into the main file and used to verify whether the codes are valid or not.
"""

def get_digit(number, position): # Gets the digit from a specific position.
  '''This function accepts 2 arguments. It determines what the position of a specific number in the digit is. It returns the digit as an interger at the specified position.'''
  digit = (10 ** position)
  return (number // digit) % 10
                                            
def is_UPC12(number): # Calculates whether the UPC code given by the user is valid or not.
  '''This functiond accepts 1 argument. It calls get_digit to determine the position of each specific digit. It returns the Boolean value True if the check digit is equal to the last number of the UPC code and it returns False otherwise.'''
  totalOdd = get_digit(number, 1) + get_digit(number, 3) + get_digit(number, 5) + get_digit(number, 7) + get_digit(number, 9) + get_digit(number, 11)
  totalOdd = totalOdd * 3
  totalEven = get_digit(number, 2) + get_digit(number, 4) + get_digit(number, 6) + get_digit(number, 8) + get_digit(number, 10)
  digitTotal = totalOdd + totalEven
  checkDigit = 10 - get_digit(digitTotal, 0)
  if checkDigit == get_digit(number, 0):
    return True
  else:
    return False

def is_ISBN10(number): # Calculates whether the ISBN code given by the user is valid or not.
  '''This function accepts 1 argument. It also calls get_digit to determine the position of each digit. It returns the Boolean value True if the remainder is equal to the check digit of the ISBN code and it returns False otherwise.'''
  totalDigit = (get_digit(number, 9) * 1) + (get_digit(number, 8) * 2) + (get_digit(number, 7) * 3) + (get_digit(number, 6) * 4)+ (get_digit(number, 5) * 5) + (get_digit(number, 4) * 6) + (get_digit(number, 3) * 7) + (get_digit(number, 2) * 8) + (get_digit(number, 1) * 9)
  remainder = totalDigit % 11
  if remainder == get_digit(number, 0):
    return True
  else:
    return False
