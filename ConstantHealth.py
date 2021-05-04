# [2, 7, 11, 15], 9
# output: [0, 1]
# [4, 8, 6, -12], -6
# output: [2, 3]
# [18, 44, -37, 108, 40, -19], 84
# [1, 4]

def sum(input_array, target):
    for init_index in range(0, len(input_array)):
        if input_array[init_index] == target:
            return [init_index]
        for final_index in range(init_index + 1, len(input_array)):
            if input_array[init_index] + input_array[final_index] == target:
                return [init_index, final_index]
