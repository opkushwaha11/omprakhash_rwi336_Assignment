# ----1

# num = int(input("enter the number"))
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)

# ----2

# def vowel(char):
#     vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
#     #return char.lower() in vowels
#     if char in vowels:
#         return True
#     else:
#         return False

# char = input("Enter a character: ")
# if vowel(char):
#     print(f"The character '{char}' is a vowel.")
# else:
#     print(f"The character '{char}' is not a vowel.")

##--- 

# def is_vowel(char):
#     print("values of char is :",char)
#     switcher={
    
#         'a':True,
#         'e':True,
#         'i':True,
#         'o':True,
#         'u':True,
#         'A':True,
#         'E':True,
#         'I':True,
#         'O':True,
#         'U':True
#     }
#     return switcher.get(char,False)

# char = input("Enter a character: ")
# if is_vowel(char):
#     print(f"The character '{char}' is a vowel.")
# else:
#     print(f"The character '{char}' is not a vowel.")


# ----3

# num = 3
# while num <= 30:
#     if num != 24:
#         print(num)
#     num += 1


# ----4

# marks = float(input("Enter your marks: "))
# if marks < 0 or marks > 100:
#     print("Invalid marks entered. Marks should be between 0 and 100.")
# elif marks >= 80:
#     print("Congratulations You have achieved Distinction")
# elif marks >= 60:
#     print("Congratulations You have achieved First Class")
# elif marks >= 50:
#     print("Congratulations You have achieved Second Class")
# elif marks >= 40:
#     print("Congratulations You have passed")
# else:
#     print("Sorry you have failed")


# ----5

# total = 0
# for i in range(11, 21):
#     total += i

# print("The total of the first 10 numbers is:", total)


# ----6


# char = input("Enter a character: ")
# if char.isupper():
#     print("The character entered is an uppercase letter")
# elif char.islower():
#     print("The character entered is a lowercase letter")
# else:
#     print("The character entered is not an alphabet")



# ----7

# total = 0
# while True:
#     number = float(input("Enter a number (enter 0 to stop): "))
#     if number == 0:
#         break
#     total += number

# print("Total of all the numbers entered:", total)



# ----8


# char = input("Enter a character: ")
# if char.isalpha():
    
#     if char.isupper():
#         print("The character is uppercase.")
    
#     elif char.islower():
#         print("The character is lowercase.")
# else:
#     print("The input is not an alphabet character.")



# ----9

# fibonacci_series = [0, 1]

# for i in range(2, 10):  
#     next_number = fibonacci_series[-1] + fibonacci_series[-2]  
#     fibonacci_series.append(next_number)  
# print("Fibonacci series of 10 numbers:", fibonacci_series)



# ----10

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# print("Prime numbers from 3 to 30:")
# for number in range(3, 31):
#     if is_prime(number):
#         print(number)


# ----11


# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# number = int(input("Enter a number: "))

# if is_prime(number):
#     print(number, "is a prime number.")
# else:
#     print(number, "is not a prime number.")

