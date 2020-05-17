# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')
my_name = input()
print('It is good to meet you, ', my_name)
print('The length of your name is :', len(my_name))
print('What is your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')


# len() function
print('The length of "hello" is :', len('hello'))
print('The length of "My very energetic monster just scarfed nachos." is :', len('My very energetic monster just '
                                                                                 'scarfed nachos.'))

# str() function
s = str(30)
print('I am ' + s + ' years old.')
s = str(0)
print('The value of str(0) is :', s)

s = str(-3.14)
print('The value of str(-3.14) is :', s)

i = int('42')
print('The value of int("42") is', i)

i = int(1.25)
print('The value of int(1.25) is :', i)

i = int(1.99)
print('The value of int(1.99) is :', i)

f = float('3.14')
print('The value of float("3.14") is :', f)

f = float(10)
print('The value of float(10) is :', f)

spam = input('Enter int value :')
print('The value of "spam" is :', spam)

spam = int(spam)
print('The value of "spam" is :', spam)

print('The value of "spam * 10 / 5" is :', spam * 10 / 5)

f = int(7.7)
print('Round a floating point number down "int(7.7)" :', f)

f = int(7.7) + 1
print('Round a floating point number down "int(7.7) + 1 ":', f)

print("42 == '42' :", 42 == '42')
print("42 == 42.0 :", 42 == 42.0)
print("42.0 == 0042.000 :", 42.0 == 0042.000)
