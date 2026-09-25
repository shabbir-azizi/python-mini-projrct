num1 = float(input("enter frist number: "))
operator = input("enter operator (% * = - + /): ")
num2 = float (input("enter second number: "))
if operator == "+" :
    result = num1 + num2
elif operator =="-" :
    result = num1 - num2 
elif operator == "/":
    result = num1 / num2
elif operator =="=" :
    result = num1 = num2 
elif operator == "*":
    result = num1 * num2
elif operator == "%":
    result = num1 % num2
    if num2 != 0:
        result= num1 / num2

    else:
        result ="cannot divide by zero"




print("Result :",result)


print (True+ True)
print(True+ False)


print ("Bitwise and : 8 ", 5 & 2)

print("Bitwise or :| ", 5 | 2)

a = 5
b = 3

print(a & b)   
print(a | b)  
print(a ^ b)  
print(~a)      
print(a << 1)  
print(a >> 1)  


a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

print( 'hellow','world')
my_integer_var = 10
print('Integer:', my_integer_var)

my_float_var = 4.50
print('Float:', my_float_var)
my_string_var = 'hello'
print('String:', my_string_var)
my_integer_var = 10
print(type(my_integer_var))  

my_float_var = 4.50
print(type(my_float_var)) 

my_string_var = 'hello'
print(type(my_string_var))  

my_boolean_var = True
print(type(my_boolean_var)) 
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

# age = 20
# print(age, type(age))

# score = 80.5
# print(isinstance(score, float))

# my_str = "Hello world"

# print(my_str[0])  # H
# print(my_str[6])  # w
# print(my_str[-1])
# my_str = 'Hello world'
# print(my_str[8:])
# my_str = 'Hello world'
# print(my_str[:7])

# my_str = 'Hello world'
# print(my_str[1:4])
# my_str = 'Hello world'
# print(my_str[::-1]) # dlrow olleH
# my_str = 'hello world'

# replaced_my_str = my_str.replace('hello', 'hi')
# print(replaced_my_str)  # hi world
# my_str = '  hello world  '

# trimmed_my_str = my_str.strip()
# print(trimmed_my_str) 

# age =11
# input("what is your age :")
# if  (age >= 18 ):
#     print("you are above of 18")
message = 'Python is fun!'

print(message[0:6])  
print(message[7:])  
print(message[::2]) 