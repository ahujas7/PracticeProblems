# Given a string, check if the braces are balanced
# (each opening bracket must have a closing bracket)

def check_braces(string):
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

def two_sum(nums, target):
    hashmap = {}

    for index in range(len(nums)):
        complement = target - nums[index]

        if complement in hashmap:
            return [hashmap[complement], index]

        hashmap[nums[index]] = index
