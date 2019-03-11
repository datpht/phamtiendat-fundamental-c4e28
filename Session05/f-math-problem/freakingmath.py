from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    op = choice(['+','-','*','/'])
    result = 0
    error = randint(-1,1)

    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y
    
    display = result + error
    
    return [x, y, op, display]

def check_answer(x, y, op, result, user_choice):
    if op == '+' :
        if x + y == result:
            if user_choice == True:
                return True
            else:
                return False
        else:
            if user_choice == True:
                return False
            else:
                return True
    elif op == '-' :
        if x - y == result:
            if user_choice == True:
                return True
            else:
                return False
        else:
            if user_choice == True:
                return False
            else:
                return True
    elif op == '*' :
        if x * y == result:
            if user_choice == True:
                return True
            else:
                return False
        else:
            if user_choice == True:
                return False
            else:
                return True
    elif op == '/' :
        if x / y == result:
            if user_choice == True:
                return True
            else:
                return False
        else:
            if user_choice == True:
                return False
            else:
                return True
    pass
