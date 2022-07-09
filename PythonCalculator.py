###this is a calculator
import math

while True:
  firstselection = str(input('enter which operation you would like to use: '  ))

  if firstselection == '+':
    while True:
      secondselection = int(input('enter the first number you would like to add: ' ))
      thirdselection = int(input('enter the second number you would like to add: ' ))
      sum = secondselection + thirdselection
      print('The sum is ' + str(sum))
      fourthselection = str(input('would you like to use the addition function again? If so, type "yes". If not, type "no": ' ))
      if fourthselection == 'yes':
        continue
      else:
        break
  if firstselection == '-':
    while True:
      fifthselection = int(input('enter the first number you would like to subtract: '))
      sixthselection = int(input('enter the second number you would like to subtract: '))
      difference = fifthselection - sixthselection
      print('The difference is ' + str(difference))
      seventhselection = str(input('would you like to use the subtraction function again? If so, type "yes". If not, type "no": ' ))
      if seventhselection == 'yes':
        continue
      else:
        break
  if firstselection == '*':
    while True:
      eighthselection = int(input('enter the first number you would like to multiply: '))
      ninthselection = int(input('enter the second number you would like to multiply: '))
      product = eighthselection * ninthselection
      print('The product is ' + str(product))
      tenthselection = str(input('would you like to use the multiplication function again? If so, type "yes". If not, type "no": ' ))
      if tenthselection == 'yes':
        continue
      else:
        break
  if firstselection == '/':
    while True:
      eleventhselection = int(input('enter the first number you would like to divide: '))
      twelfthselection = int(input('enter the second number you would like to divide: '))
      quotient = eleventhselection / twelfthselection
      print('The quotient is ' + str(quotient))
      thirteenthselection = str(input('would you like to use the division function again? If so, type "yes". If not, type "no": ' ))
      if thirteenthselection == 'yes':
        continue
      else:
        break
