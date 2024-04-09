#----1

# def add():
#     print("Function add() called")

# def modify():
#     print("Function modify() called.")

# def delete():
#     print("Function delete() called.")

# def main():
#     user_input = int(input("Enter a number (1 for add, 2 for modify, 3 for delete): "))
    
#     match user_input:
#         case 1:
#             add()
#         case 2:
#             modify()
#         case 3:
#             delete()
#         case _:
#             print("invalid Please enter 1, 2, or 3")
# main()


#----2

# def square_number(num):
#     return num ** 2
# num = int(input("enetr the number"))
# result = square_number(num)
# print("Square of", num, "is", result)


#----3

# def display(char, num, string):
#     print("character:", char)
#     print("integer:", num)
#     print("string:", string)

# display('a', 10, "hello, world")


#----4

# def myfun1():
#     print("this is myfun1()")

# def myfun2():
#     print("this is myfun2()")
#     myfun1()
    
# myfun2()


#----5

# def check_number(number):
#     if number > 0:
#         return 1
#     elif number < 0:
#         return -1
#     else:
#         return 0

# num1=int(input("check_number"))
# print(check_number(num1))

# num2=int(input("check_number"))
# print(check_number(num2))

# num3=int(input("check_number"))
# print(check_number(num3))

# print(check_number(5))
# print(check_number(-3)) 
# print(check_number(0))  


#---6

# def toggle_character(char):
#     if char.islower():
#         return char.upper()
#     elif char.isupper():
#         return char.lower()
#     else:
#         return char

# print(toggle_character('a'))  
# print(toggle_character('B'))  
# print(toggle_character('5'))  


#----7

# def toggle_string(string):
#     return string.swapcase()

# print(toggle_string("Hello, World!")) 
# print(toggle_string("tOgGlE"))         


#---8

# def validate_string_length(string, min_length=3, max_length=5):
#     if len(string) < min_length:
#         return "string length is less than the minimum allowed length of {}".format(min_length)
#     elif len(string) > max_length:
#         return "string length exceeds the maximum allowed length of {}".format(max_length)
#     else:
#         return "string length is within the acceptable range"


# print(validate_string_length("hello"))     
# print(validate_string_length("hi"))         
# print(validate_string_length("python"))     
# print(validate_string_length("worlds"))     


#----9

def calculate_sum(*args):
    total = sum(args)
    print("sum of the values:", total)

calculate_sum(1, 2, 3, 4, 5)         
calculate_sum(10, 20, 30, 40, 50, 60)  
calculate_sum(2, 4, 6)                 

