'''
import os
from tempfile import TemporaryFile

if os.path.exists('WebScraping/html'):
    print("Data is exists")
else:
    print("It has there")

with TemporaryFile('w+') as tobj:
    tobj.write("Hello, dear, i'm Here.")

    #tobj.seek(0)
    tobj.seek(7)
    data = tobj.read()
    print(data)

name = input("Enter your name: ")
characters = 'abcdefghijklmnopqrstuvwxyz'
total_char = len(name)
print(total_char)

import pyinotify

# property set kora
import time
class Prosenjit:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last


    @property
    def email(self):
        return '{}.{}.gmail.com'.format(self.firstname, self.lastname)


    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)


    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(' ')
        self.firstname = firstname
        self.lastname = lastname

# akhane fullname name 3 ta method ache and ak aktar property akak rokom
    # prottektate tar variabler property chang hoeche
    # generally simple method call kora hoy avbae fullname() and property method call
    # kora hoy fullname kono () hobe na. :(

    @fullname.deleter
    def fullname(self):
        print("Name is Deleted")
        self.firstname = None
        self.lastname = None
        self.end_t = time.time()

start_t = time.time()
pro = Prosenjit('Prosenjit', 'Kumar')
pro.fullname = 'Chandrajit Kumar'
print('Firstname: ',pro.firstname)
print('Email: ',pro.email)
print('Fullname: ',pro.fullname)
del pro.fullname

print("Start Time need: ", str((start_t)/1000), "Mil Sec")
print("End Time need: ", str((pro.end_t)/1000), "Mil Sec")
'''


def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


if __name__ == "__main__":
    my_decorator()