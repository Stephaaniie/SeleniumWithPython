'''Write a program that validates if the x value is less than 10, knowing that x=15.
- Iterate the operation until the condition is true.
- The expected value must be printed.'''

x = 15

def restaHasta10(numero):
    if numero < 10:
        return numero
    return restaHasta10(numero-1)

print(restaHasta10(x))

def restaHasta10ConWhile(numero):
    while numero >= 10 : 
        numero = numero - 1
    return numero

print('El numero x = ' + str(x) +' Ahora vale: ' + str(restaHasta10ConWhile(x)))

def restaHasta10ConFor(num):
    for num in range(11):
        num = num - 1
    return num

print('El numero x = ' + str(x) +' Ahora vale: ' + str(restaHasta10ConFor(x)))

'''Exercise 2
- Create a class(Person) with at least one class attribute, use the __init__() function to assign values to the instance and class attributes.
- Create a method (Shout) print the shout along with the name of the person doing it.'''

class Person:
    def __init__(self, name):
        self.name = name
    def shout(self):
        print('Hola buenas tardes ' + x.name);


x = Person('Stephanie')
x.shout()

