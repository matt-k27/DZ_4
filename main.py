print('DZ4')

inputtedNumber1 = float(input('Please enter first number : '))
inputtedNumber2 = float(input('Please enter second number : '))
inputtedAction = str(input('Please enter action : '))

if inputtedAction == '+':
    print(inputtedNumber1 + inputtedNumber2)
elif inputtedAction == '-':
    print(inputtedNumber1 - inputtedNumber2)
elif inputtedAction == '*':
    print(inputtedNumber1 * inputtedNumber2)
elif inputtedAction == '/':
    if inputtedNumber2 == 0:
        print('You can\'t divide by 0')
    else:
        print(inputtedNumber1 / inputtedNumber2)
else:
    print('Invalid')

print('Thank you for using')