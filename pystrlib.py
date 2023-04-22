import googletrans
from googletrans import Translator


send_info = """
PSL stands for Python String Library
This Library has 2 Methods:
    .parse
    .modify
.parse parses through the string given by the user
.parse is expected to have 2 arguments
1st argument should be the string that needs to be parsed
2nd argument can be 'len', 'case' & 'repeat'

.PARSE (
LEN [
    len: returns the length of the string
]

CASE [
    case: returns how many upper case and lower case 
    charecters are present
]

REPEAT [
    repeat: needs to have a charecter after 'repeat: '
    eg. 'repeat: a'
    this returns how many times 'a' is present in the string
    you can also use special arguments within repeat
    they are "_string_", "_most_" & "_least_".

    _string_: returns how many times a charecter has 
    occurred in the string
    _most_: returns the charecter which occurred the 
    most in the string
    _least_: returns the charecter which occurred the 
    least in the string
]
)

.modify has 4 arguments in it
they are:
    'up'
    'down'
    'reverse-case'
    'remove: '

.MODIFY (
    up: returns the whole string in upper case
    down: returns the whole string in lower case
    reverse-case: switches the case of all the 
    charecters in the string
    remove:: remove argument is expecting a character after the colon and 
    that charecter will be removed from the string and will be returned 


)
"""


def parse(u,event):
    if event == None:
        return u

    elif event == 'len':
        return len(u)

    elif event == 'case':
        a = 0
        b = 0
        for i in u:
            if i.isupper():
                a = a + 1
                
            elif i.islower():
                b = b + 1
                
            elif i == ' ':
                pass
            
            else:
                return "Invalid Input(s)"
        main = f'''Upper Case: {a}
Lower Case: {b}'''
        return main

    elif event[0:7] == 'repeat:':
        event = event.split(':')
        arg = event[1]
        arg = arg.lstrip()
        if arg == '_string_':
            char = {}
            for i in u:
                if i in char:
                    char[i] = char[i] + 1
                elif i not in char:
                    char[i] = 1
                else:
                    return "Invalid Input(s)"
            return char

        elif arg == '_most_':
            char = {}
            for i in u:
                if i in char:
                    char[i] = char[i] + 1
                elif i not in char:
                    char[i] = 1
                else:
                    return "Invalid Input(s)"

            positions = [] 
            max_value = 0
            for k, v in char.items():
                if v == max_value:
                    positions.append(f"{k}:{v}")
                if v > max_value:
                    max_value = v
                    positions = [] 
                    positions.append(f"{k}:{v}")

            return positions

        elif arg == '_least_':
            char = {}
            for i in u:
                if i in char:
                    char[i] = char[i] + 1
                elif i not in char:
                    char[i] = 1
                else:
                    return "Invalid Input(s)"

            positions = [] 
            min_value = float("inf")
            for k, v in char.items():
                if v == min_value:
                    positions.append(f"{k}:{v}")
                if v < min_value:
                    min_value = v
                    positions = [] 
                    positions.append(f"{k}:{v}")


            return True

        else:

            a = 0
            for i in u:
                if i == arg:
                    a = a + 1
                else:
                    continue

            if arg in u:
                return a
            else:
                return False
    else:
        return "Invalid argument(s)"

def modify(u, event):

    if event == None:
        return u
    elif event == 'up':
        return u.upper()

    elif event == 'down':
        return u.lower()
 
    elif event == 'reverse-case':
        return u.swapcase()

    elif event[0:7] == 'remove:':
        arg = event.split(':')
        arg = arg[1]
        arg = arg.lstrip()
        arg = arg.rstrip()
        return  u.replace(arg, '')
    
    else:
        return "Invalid Argument(s)"
    
def info():
    return send_info