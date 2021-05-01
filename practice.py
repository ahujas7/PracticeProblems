# Check for balanced braces
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