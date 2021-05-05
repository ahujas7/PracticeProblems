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


# Max number of balls in a box

def countBalls(low_limit, high_limit):
    boxes = {}

    for ball in range(low_limit, high_limit + 1):
        box_num = 0
        for char in str(ball):
            box_num += int(char)
        if box_num in boxes:
            boxes[box_num] += 1
        else:
            boxes[box_num] = 1

    max = 0
    for element in boxes:
        if boxes[element] > max:
            max = boxes[element]

    return max


# Subtract the Product and Sum of Digits of an Integer

def subtractProductAndSum(n):
    sum = 0
    product = 1
    for char in str(n):
        sum += int(char)
        product *= int(char)

    return product - sum


# Number of Lines To Write String
# New function used: ord() - returns integer
# for inputted unicode character (inverse
# of ord() is chr()

def numberOfLines(widths, s):
    total = 0
    lines = 1

    for char in s:
        w = widths[ord(char) - ord('a')]
        if total + w > 100:
            lines += 1
            total = 0
        total += w

    return [lines, total]


# Given a positive integer num, output its complement
# number. The complement strategy is to
# flip the bits of its binary representation.

def findComplement(num):
    string = str(bin(num))[2:]
    complement = 0

    for i in range(0, len(string)):
        if string[i] == '0':
            complement += 2 ** (len(string) - i - 1)

    return complement


# Format License Keys

def licenseKeyFormatting(s, k):
    string = ''.join(s.split('-'))
    output = ''

    output += string[0:len(string) % k]

    for i in range(len(string) % k, len(string), k):

        if output != '':
            output += '-'

        output += string[i:(i + k)]

    return output.upper()


# Check if it is a straight line

def isStraightLine(coordinates):
    prev_rise = abs(coordinates[1][1] - coordinates[0][1])
    prev_run = abs(coordinates[1][0] - coordinates[0][0])

    for i in range(1, len(coordinates) - 1):
        curr_rise = abs(coordinates[i + 1][1] - coordinates[i][1])
        curr_run = abs(coordinates[i + 1][0] - coordinates[i][0])
        if curr_rise != prev_rise or curr_run != prev_run:
            return False
        prev_rise = curr_rise
        prev_run = curr_run

    return True



