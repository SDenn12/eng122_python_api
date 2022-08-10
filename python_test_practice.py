def user_name():
    pass

def loop_array():
    arr = [1,2,3,4,5]
    for item in arr:
        print(item)

# you can use boolean operators: | or, & and, not. &&, || determine if something is 'truthy or falsy'

# lists are mutable, tuples are immutable

# you can't add elements to tuples as they are immutable

# you can have multiple types of data in a tuple

# data type is a dictionary

class DevOps:
    pass
object_ = DevOps()

def append_(arr= [1,2,3,4]):
    arr.append(5)
    return arr

def arguments(arg):
    if arg == "devops":
        return True
    return False

class ClassZ:
    pass

class ClassY(ClassZ):
    def __init__(self):
        super().__init__()

def odd_even(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            if (i + 1) % 2 == 0:
                return True
            else:
                return False
        else:
            return None


def percentage(value1,value2):
    if value1 | value2 == 0:
        v_1 = int(input("Enter a new number. "))
        v_2 = int(input("Enter a new number. "))
        percentage(v_1,v_2)
    return 100 * value1 / value2

def divide(value1,value2):
    if value1 | value2 == 0:
        v_1 = int(input("Enter a new number. "))
        v_2 = int(input("Enter a new number. "))
        divide(v_1,v_2)
    return value1/value2

def dob(day, month):
    if day < 1:
        v_1 = int(input("Enter a day. "))
        v_2 = int(input("Enter a month. "))
        day, month = dob(v_1, v_2)
    return day, month

print(dob(0,12))

def multiply(value1, value2):
    if value1 | value2 == 0:
        v_1 = int(input("Enter a new number. "))
        v_2 = int(input("Enter a new number. "))
        multiply(v_1,v_2)

    return value1 * value2

def find_odd_even(lst):
    """finds locations of odd and even numbers in a list"""
    even_lst = []
    odd_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    return even_lst, odd_lst

def bill():
    shopping_lst = {
        "milk": 3.4,
        "potato": 5.5,
        "bread": 6,
        "butter": 7,
        "cookies": 5.4
    }
    total = 0
    for key, value in shopping_lst.items():
        total += value
    return total

