from art import logo
print(logo)
#Add 
def add(n1, n2) :
    return n1 + n2

#Substrate 
def subs(n1, n2) :
    return n1 - n2

#Multiply 
def mul(n1, n2) :
    return n1 * n2

#Divide 
def divide(n1, n2) :
    return n1 / n2

#Dictionaries 

operations = {
    "+" :  add ,
    "-" : subs ,
    "*" : mul ,
    "/" : divide 
}
#
#while should_continue :
def Calculator():
    num1 = float(input('Type the first number to operate: '))
    for i in operations :
        print(i)
    should_continue = True 
    while should_continue :       
        operation_symbol = input('Choose a symbol from the symbols showed above:\n')
        num2 = float(input('Type the next number to operate: '))
        #print(operation_symbol)
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}.') 
        #Trying to reach out the program
        #Presione Si para hacer otro cálculo con el numero anteriormente calculado o n para hacer otro cálculo
        if input('Do you want to made another operation with {answer} or do you want to made another new operation? Type "y" by yes or "n" to have another calculation' ).lower() == 'y' :
            num1 = answer
        
        else :
            should_continue = False        
            Calculator()
Calculator()
