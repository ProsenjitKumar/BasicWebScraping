# print(*range(1, int(input()) + 1), sep="")

# print(*range(0,9 -5), sep='9')


# total time need a1 = 12 minutes for fill up for drums
# every per mintue a2 = 15 L to out of drums
# if a2 nall is open then it will fill up to take 48 minutes
# so about how many water to catch in this drums?

'''
a1 = (input("Input Your 1 pipe to take time(minutes): "))
amount1 = int(input("And your out of water quantity: "))
a2 = int(input("Input 2 pipe to take time(minutes): "))
amount2 = int(input("And your out of water quantity: "))
# filled_up_without_hole = int(input("Filled Up without any hole quantity: "))
filled_up_without_hole_time = int(input("Filled Up Time(minutes): "))
# filled_up_with_1_hole = int(input("Filled Up with 1 hole quantity: "))
filled_up_with_hole_time = int(input("Filled Up Time(minutes): "))


catch_to_filled_up_drums_total =

# decorator

from Test import my_decorator

@my_decorator
def sending_method():
    c = print("ure ase jure bosechi")
    a = [1,2,3,4,5,6,9,8,7]
    all_add = str(sum(a))
    print(all_add )


sending_method()


import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())

#from boltons.funcutils import wraps

def decorator(some_function):
    #@wraps(some_function)
    def wrapper():
        print("This is printed before call the function.")
        some_function()
        print("This is printed after call the function.")
    return wrapper

def my_function():
    print("This is the function!")

my_function = decorator(my_function)

my_function()

'''


class Pr:


    def kptha(self):
        print("lalal")
        return self.lol()

    def lol(self):
        print("nananan")

pro = Pr()
pro.kptha()




