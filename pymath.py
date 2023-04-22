inv = "Invalid Input(s)"

def addpy(*args):
    sum_ = 0
    try:
        for i in args:
            
            if i == None:
                pass
            else:
                sum_ = sum_ + i
        return round(sum_, 4)
    except:
        return inv

def subpy(*args):
    num = args[0]
    try:
        for i in args[1:]:
            num = num - i
        return round(num, 4)
    except:
        return inv

def multipy(*args):
    num = args[0]
    try: 
        for i in args[1:]:
            num = num * i
        return round(num, 4)
    except:
        return inv

def powpy(*args):
    try:
        if len(args) > 2:
            return f"{inv}, Only 2 numbers are expected"
        elif len(args) == 2:
            ans = args[0]**args[1]
            return ans
        else:
            return 'Inputs are less than 2'
    except:
        return inv

def divpy(num1, num2):
    try:
        number = num1/num2
        return round(number, 4)
    except ZeroDivisionError:
        return f"{inv} | Cannot divide a number with 0"
    except:
        return inv

def rootpy(number, num):
    try:
        numb = num**(1/number)
        return round(numb, 4)
    except:
        return inv

def modpy(num1, num2):
    try:
        num = num1%num2
        return round(num, 4)
    except:
        return inv

def meanpy(*args):
    mean_ = 0
    try:
        for i in args:
            
            if i == None:
                return inv
            else:
                mean_ = mean_ + i

            mean = mean_/len(args)
        return round(mean, 4)
    except:
        return inv

def factpy(num):
    try: 
        fact = 1
  
        for i in range(1, num+1):
            fact = fact * i 

        return fact

    except:
        return inv

def stdevpy(*args):
    try: 
        len_args = len(args)
        main = []
        mean_ = 0
        
        for i in args:      
            mean_ = mean_ + i
        mean = mean_/len(args)

        for b in args:
            a = (x[b]-mean)**2
            main.append(a)

        return main
    except:
        return inv
    
def fibonacci_seq(num, till_last):
    try:
        num = int(num)
        if num <= 0:
            return 0

        elif num >= 1:
            if till_last == True:
                a, b = 0, 1
                li = []
                while a < num:
                    li.append(a)
                    a, b = b, a+b
                return li
                

            elif till_last == False:
                a = 0
                b = 1
                for i in range(1, num):
                    c = a + b
                    a = b
                    b = c
                return b

            else:
                return inv
        else:
            return inv


    except ValueError:
        return 'Argument is expected to be an int'
    
    



def infopy():
    s1 = "This is a Math Module made by Sai"
    s2 = "There are a lot of math operations available"
    s3 = "Addition: addpy"
    s4 = "Subtraction: subpy"
    s5 = "Multiplication: multipy"
    s6 = "Power by any number: powby"
    s7 = "Division: divpy"
    s8 = "Root by any number: rootpy"
    s9 = "Reminder of numbers: modpy"
    more = "More comming soon..."
    statement = f'{s1}\n{s2}\n{s3}\n{s4}\n{s5}\n{s6}\n{s7}\n{s8}\n{s9}'
    return statement

