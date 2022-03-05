"""
Name: Merathy Romain
Date: December 14, 2021
Description: Write a program that is able to determine whether a 12 digit UPC code or a 10 digit ISBN code is valid or not. Create a checkdigits module that will hold three functions named get_digit, is_UPC12 and is_ISBN10. The main file should hold the main function and the menu function. The checkdigits module should be imported into the main file and used to verify whether the codes are valid or not. 
"""

import checkdigits

def main(): # Gathers input for the user's choice and determines whether the UPC code or the ISBN code is valid or not.
  '''This function does not have any paramters. It calls the menu function and prompts the user for their choice. It displays "Valid" or "Not Valid" when the user enters the appropriate code. It does not return any values.'''
  menu()
  choice = ""
  s = True
  while s:
    choice = input("\nChoice: ")
    if choice == "1": # Determines whether the ISBN code is valid or not.
      isbn10 = int(input("\nPlease enter a 10 digit ISBN code: "))
      isbnDigit = checkdigits.is_ISBN10(isbn10)
      if isbnDigit:
        print("Valid")
      else:
        print("Not Valid")
      menu()
    elif choice == "2": # Determines whether the UPC code is valid or not.
      upc12 = int(input("\nPlease enter a 12 digit UPC code: "))
      upcDigit = checkdigits.is_UPC12(upc12)
      if upcDigit:
        print("Valid")
      else:
        print("Not Valid")
      menu()
    elif choice == "Q" or choice == "q": # Quits the program when the user enters 'Q' or 'q'.
      print("\nExiting The Program...")
      break
    else:
      menu()
      print("\nThat is not a valid option. Please try again.")

def menu(): # Displays a menu
  '''This function does not have any parameters. It displays a menu of options for the user and does not return any values.'''
  print("\nCHECK DIGIT VALIDATOR")
  print("\n1. ISBN-10")
  print("2. UPC-12")
  print("Q. Quit Program")

main()
