# Given a string, check if the braces are balanced
# (each opening bracket must have a closing bracket)

def checkBalancedBraces(string):
    char_list = []

    for i in string:
        if i == '(' or i == "[" or i == "{":
            char_list.append(i)
        elif i == ')' or i == "]" or i == "}":
            try:
                char_list.pop()
            except IndexError:
                return False

    if len(char_list) == 0:
        return True
    else:
        return False


# Given a list of integer pairs and one unique
# integer, find the unique integer

def exists(input_list):
    hashmap = {}

    for element in input_list:
        if element not in hashmap:
            hashmap[element] = 1
        else:
            hashmap[element] += 1

    for key in hashmap.keys():
        if hashmap.get(key) == 1:
            return key


# Given an array of integers nums and an integer
# target, return indices of the two numbers
# such that they add up to target
# O(n^2) solution:
# for index_i in range(len(nums)):
#     for index_f in range(index_i + 1, len(nums)):
#         if nums[index_i] + nums[index_f] == target:
#             return [index_i, index_f]

def twoSum(nums, target):
    hashmap = {}

    for index in range(len(nums)):
        complement = target - nums[index]

        if complement in hashmap:
            return [hashmap[complement], index]

        hashmap[nums[index]] = index


# Self Dividing Numbers
# Find the numbers that are divisible
# by each of their digits (R = 0) in a given range

def selfDividingNumbers(left, right):
    numbers = []
    for num in range(left, right + 1):
        is_self_dividing = True

        if '0' in str(num):
            continue

        for digit in str(num):
            if num % int(digit) != 0:
                is_self_dividing = False
                break

        if is_self_dividing:
            numbers.append(num)

    return numbers


# Sum of digits in Base k
# Given an integer in base 10 and a base k,
# return the sum of the digits of n after being
# converted to base k

def sumBase(n, base):
    quotient = n
    sum = 0

    while quotient >= base:
        sum += quotient % base
        quotient = quotient // base

    sum += quotient
    return sum
