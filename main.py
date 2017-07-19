# Author: Taylor Hoss
# Date:   6/22/2016
# Description: This program randomly generates numbers to be used in specific arithmetic drills

# importing randint from random library
from random import randint


# converts a list of characters 0-9 to an int
def list_to_int(lst):
    num = 0
    for i in lst:
        num = (num * 10) + int(i)
    return num


# remove all zeroes, ones, twos, and threes from an int
def rmv_zero_to_three(num):
    lst = list(str(num))                     # converts given number to string and then turns it into a list
    k = 0                                    # sets counter

    for n in lst:                            # iterates through list
        if n in ['0', '1', '2', '3']:    # if it finds a 0-3 inclusive within, it changes it to a larger number
            lst[k] = str(randint(4, 9))
        k += 1

    new_num = list_to_int(lst)              # convert list of strings to int

    return new_num                          # return


# addition
print("Addition")

for x in range(0, 13):
    print(rmv_zero_to_three(randint(1000, 9999)))

# multiplication
print("\nMultiplication")

print(randint(1000000, 9999999), "*", randint(100, 999))

# Division
print("\nDivision")

print(randint(10000000, 99999999), "/", randint(10, 99))

