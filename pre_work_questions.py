#1 write a funciton to print "hello_username"

def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user("bernadette")

#2 print all odd number 1 to 100 and returns nothing

def first_odds():
    for odd_num in range(1, 100, 2):
        print(odd_num)

#3 write a function for maximum number in a list to return the max number in the list

def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])

max_num_in_list([1,2,4,67,8])

#4 write a function to return if the given year is a leap year
    #leap year is divisible by 4 but not 100 (unless 400)

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

#5 write a function to see if all number in a list are consecutive numbers
    # [2,3,4,5,6] is consecutive [1,2,4,5] is not. 

def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list) + 1)):
        return True
    else:
        return False

is_consecutive([2, 6, 3, 1, 5, 4, 10])
