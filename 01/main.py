""" main.py

Resistor expression calculator

written after a full bottle of jack
shitty code ahead

"""

import os
import string

user_input = ""
valid_expression = ""
result = 0.00
ended_session = False
is_input_valid = False
exit_keywords = ["Exit","E","e","exit","EXit"]

def get_userInput():
    print("Type your expression or 'exit' to exit: ")
    global user_input
    user_input = input()
    user_input = user_input.replace(" ","")

def get_valid_input():
    global is_input_valid
    if exit_keywords.count(user_input) > 0: return "Exiting..."
    
    #search for illegal inputs
    for chr in user_input:
        _valid_chairs_count = chr.count("+") + chr.count("(") + chr.count(")") + chr.count("/")

        if not chr.isdecimal() or not chr.isdigit():
            if not _valid_chairs_count > 0: 
                return "Illegal characters detected."
    
    #check for parenthesis mistakes
    #TODO: improve opening and closing position mistakes
    if not user_input.count("(") == user_input.count(")"): return "Parenthesis mistakes detected." 

    #TODO: check for order of operation mistakes

    is_input_valid = True
    return user_input.replace(" ","")

def solve_expression():
    if not is_input_valid: return
    global valid_expression

    #solve the parenthesis in complex expressions
    while valid_expression.count("(") > 0:
        chrid = 0
        _p_expression = ""
        _new_p_expression = ""
        for chr in valid_expression:
            if chr == "(" and valid_expression[chrid + 1] != "(":

                #get the expression that is inside the parenthesis
                if valid_expression[chrid + 1] == "(": continue

                for pchar in range(len(valid_expression)):
                    if valid_expression[chrid + pchar] == ")":
                        _p_expression = _p_expression + ")"
                        break
                    elif valid_expression[(chrid + pchar)+1] == "(": #prioritize parenthesis futher ahead
                        _p_expression = ""
                        continue
                    else: _p_expression =_p_expression + valid_expression[chrid + pchar]
            chrid += 1
            if _p_expression != "": break #found an expression between parenthesis

        #solve the expression inside the parenthesis and replace with in the original expression
        if _p_expression.count("+") > 0: #series
            _new_p_expression = str(eval(_p_expression))

        if _p_expression.count("/") > 0: #parallel
            _new_p_expression = _p_expression.replace("//","+")
            _new_p_expression = _new_p_expression + "**-1"

            _temp_p_expression = ""
            for chr in range(len(_new_p_expression)):

                if _new_p_expression[chr] == "+" or _new_p_expression[chr] == ")":
                    _temp_p_expression = _temp_p_expression + "**-1"

                _temp_p_expression = _temp_p_expression + _new_p_expression[chr]
           
            _new_p_expression = _temp_p_expression
            _new_p_expression = str(eval(_new_p_expression))


        valid_expression = valid_expression.replace(_p_expression,_new_p_expression)
        
        #print(valid_expression)

        
        #return
    
    #solve only series resistance
    if valid_expression.count("+") > 0:
        return eval(valid_expression)

    #solve only parallel resistance
    if valid_expression.count("/") > 0:
        _temp_value = ""
        _formated_expression = valid_expression.replace("//","+")
        for chr in range(len(_formated_expression)):
            if _formated_expression[chr] == "+":
                _temp_value = _temp_value + "**-1"
            
            _temp_value = _temp_value + _formated_expression[chr]
        _temp_value = _temp_value + "**-1"
        _temp_value = "(" + _temp_value + ")**-1"

        return eval(_temp_value)
    
    return valid_expression

while not ended_session:
    print("\n")
    get_userInput()
    valid_expression= get_valid_input()
    
    #print("\n")
    print(valid_expression)
    _result = solve_expression()

    print("Is the same as " + str(_result) + "R")

    ended_session = exit_keywords.count(user_input) > 0

    if _result != None:
        pass

    #os.system("clear")

    

    

    
