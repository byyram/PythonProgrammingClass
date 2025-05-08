print('Enter two integers, and I will tell you', 
      'the relationships they satisfy.')

num1 = int(input("Gimme the first number: "))
num2 = int(input("Gimme the second number: "))

if num1 == num2:
    print(num1, 'is equal to', num2)
else:
    print(num1, 'is not equal to', num2)

if num1 >= num2:
    print(num1, 'is greater than or equal to', num2)
else:
    print(num1, 'is less than', num2)

if num2 >= num1:
    print(num2, 'is greater than or equal to', num1)
else:
    print(num2, 'is less than', num1)