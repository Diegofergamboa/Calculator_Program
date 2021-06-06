"from art import logo"
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
num1 = int(input('Type the first number to operate: '))
num2 = int(input('Type the second number to operate: '))
for i in operations :
    print(i)
    
operation_symbol = input('Choose any of the symbols showed above:\n')
#print(operation_symbol)
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f'The result of the operation is, {answer} ') 
