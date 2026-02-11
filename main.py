# a = 12

# print(12/3)



# print(bool(a))


# name = "keval"

# age = "20"

# print(name,age)

# -----------------------------------string and type convesion------------------------


# a = 128522

# print(chr(a))


# a = "S"

# print(ord(a))


# a = "Kenil Gelani"

# print(a[-1],a[3])


# a = int(input("Tell me your number :- "))


# num = int(input("Tell me number :- "))

# if num%2 == 0:
#    print("even number")

# else:
#    print("odd number")

# name = input("Enter your name :- ")
# age = int(input("Enter your age :- "))

# if age >= 18:
#    print(f"hello {name} you are a valid vote")

# else:
#    print(f"hello {name} you are a not valid vote")




# year = int(input("Tell your Year:- "))

# if year %100 == 0 and year % 400 == 0:
#     print("Tts leap year")

# elif year % 100 != 0 and year % 4 == 0:
#     print("Its leap year")

# else:
#     print("Its Normal year")



# t = int(input("Pelase tell me tempature:- "))

# if t < 0:
#    print("Frezzing cold")

# elif t >= 0 and t < 10:
#    print("very cold")

# elif t >= 10 and t < 20:
#    print("cold")

# elif t >= 20 and t < 30:
#    print("pleasant")

# elif t >= 30 and t < 40:
#    print("Hot")

# else:
#    print("Very Hot")








# import random

# num = random.randint(1,4)

# print(num)

# a = int(input(" enter the number :- "))

# if a == 10:
#     print("win cholclate")

# elif a == 20:
#     print('win ice cream')

# else:
#     print("win cake ")




# num1 = int(input("Please tell your first number:-"))
# num2 = int(input("please tell your Second number:- "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both number are same")




# gender = input(" please tell your gender as character (M or F):- ")

# if gender == 'M' or gender == 'm':
#     print("Good moring SIR")

# elif gender == 'F' or gender == 'f':
#     print("Good morning MAM")

# else:
#     print("unidentified gender")




# num = int(input("Please tell your number :-"))

# if num%2 ==0:
#     print("even number")
# else:
#     print("odd number")

      

# for loop



# for i in range(23):
#     print(i)

# for i in range(-3,-16,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)


# n = int(input(" Which table you want :-"))

# for i in range(n,(n*10)+1,n):
#     print(i)
             


#           loops for string



# a = "KEVAL IS A DEVLOPER"

# for i in range(len(a)):
#     print(a[i])

# a = "KEVAL IS ML DEVLOPER"

# for i in a:
#     print(i)


#           Break Continue else

# for i in range(1,21):
#     if i == 15:
#         break
#     print(i)

# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)    



#         QUESTIONS

# n = int(input(" Tell me number :- "))

# for i in range(n):
#     print("NAMASTE KESE HO AAP")



# n = int(input(" Which Table You Want :- "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")





# n = int(input("please Tell your number :-"))

# sum = 0

# for i in range(1,n+1):
#     sum += i

#     print(f"your sum is {sum}")


# n = int(input("please Tell your number :-"))

# factorial = 1

# for i in range(1,n+1):
#     factorial *= i

#     print(f"your factorial is {factorial}")  
  




# n = int(input("Which number factor you want ? : - "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

# n = int(input(" Check your number perfect or not : - "))
# sum = 0

# for i in range(1,n):
#     if n%i ==0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")       





# n = int(input("Check your number prime or not :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i ==0:
#         count += 1

# if count == 2:
#     print(" Your number is prime ")
# else:
#     print("Your number is not a prime")        




# a ="KEVAL"

# for i in range(len(a)-1,-1,-1):
#     print(a[i])



# a ="KEVAL"
# b =""
# for i in range(len(a)-1,-1,-1):
#     b = b +a[i]

# print(b)



#                  STRING IS PALLINDROME OR NOT ?


# a ="NAMAN"
# b =""
# for i in range(len(a)-1,-1,-1):
#     b = b +a[i]

# if b ==a:
#     print("your string is a pallindrome")
# else:
#     print("your string not a pallindrome")



# a = "#kevfdfgal$2443678567@%*+"

# char = 0
# digit = 0
# spchar = 0

# for i in a:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchar += 1

# print(f"your digit are {digit}\n your alphabates are {char}\n your special charcters are {spchar}")         




#                 while loop  

# a = 1

# while a <=30:
#     print(a)
#     a += 1



# -------------------------------------------  questions  --------------------------------------------------



# seprate each digit of a number and print it on the new line.

# a = int(input("Tell me number : - "))

# while a > 0:
#     print(a % 10)
#     a = a // 10



#  Accept a number and print its reverse.  ------->  EX . 576 -- (6 * 10 + 7) = 67 , -- (67 * 10 + 5 ) = 675


# a = int(input("Tell me number : - "))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)



# Accept a number and check if it is a pallindromic number(if number and its reverse and equal)


# a = int(input("Tell me number : - "))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if copy == rev:
#     print("Its a pallindromic number")
# else:
#     print("Its a not a pallindromic number")



# Create a random number guessing game with python.

# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("Please guess the number between 1 to 10 :- "))
#     if num == guess:
#         tries += 1
#         print(f"you are right guessing the number is {tries} tries")
#         break

#     elif num < guess:
#         print(" go to little number")
#         tries += 1

#     elif num > guess:
#         print("go to higher number")
#         tries += 1

#     else:
#         tries += 1
#         print("sorry you are wrong")



# -------------------------------------------------------------------------------------------------------------------

#                              what are function 

# def hello():
#         print("Hello how are you !")
        
# hello()


#  ------------------ function parameter and arguments-------------------------


# def sum(a,b):
#     print(f"The sum of your number is {a+b}")

# sum(12,12)  

# --------------------- Types of arguments ------------------------------


# def hello(name,age):
#     print(f"Your name is {name} and age is {age}")

# hello(age = 21,name = "Keval")    



# def pallindrome(st):
#     rev =""

#     for i in range(len(st)-1,-1,-1):
#         rev += st[i]

#     if rev ==st:
#         print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is not a pallindrome")    

# pallindrome("KEVAL")
# pallindrome("NAMAN")


#   ----------------------       Data Structure     ----------------------------------------   #



#                      in-built types of DS   1) List , 2)Tuple , 3)Dictionary , 4)set

#                Custom  ds ----  Queue, Linked List, Graph etc,.......


# -------------------------------------------------------------------------------------------------------


# a = [12,13,14,15,16,17.7]

# 1 st way using index


# for i in range(len(a)):
#     print(a[i])



# 2 nd way of directly on values


# for i in a:
#     print(i)    

#       ---------------- help(list) -----------------------


# l = [1,2,3,4,5,6,7,8]

# l.append(9)
# l.append(10)

# print(l)

# l = [1,2,3,4,5,6,7,9]  #  yaha pe aapko jo insert karna hai wo number ke aage wale me 0 se start kare(,yaha aap jo insert karna hai wo number likhe)
# l.insert(7,8)
# print(l)



# l = [1,2,3,4,5,6,7,8]

# p =(4,34,21,56)

# l.extend (p)

# print(l)



# fruits = ['banana' , 'apple' ,'cherry']

# points = (1, 4, 5, 6)

# fruits.extend(points)

# print(fruits)



# ----------- Print positive and negative element of an List. ------------------------------------


# l =[-45,34,-67,54,12,-62,47,-91]

# print("positive number")
# for i in l:
#     if i>=0:
#         print(i)

# print("negative number") 
# for i in l:
#     if i < 0:
#         print(i)       


#------------------- Mean of List element ------------

# l =[23,432,12,54,67,85,48,346,54]

# sum = 0

# for i in l:
#     sum = sum + i
# print(sum/len(l))    



# ------------ Find the gretrst element and print its index too. -----------------

# l = [23,453,37,85,35,555,43,777,85]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")        



# ------------ Find the second gretest element  -----------

# l =[12,23,43,54,64,32]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i 

# print(f"the sec_largest element is {sec_largest} and largest element is {largest}")       



# ----------   Check if List sorted or not -----------

# a =[12,13,14,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue

#     else:
#         print("your list is not sorted")
#         break   

# else:
#     print("your list is sorted")        




# ------------------------------ set ------------------------------------------------#

#                                                  1)  union


# a ={1,2,3,4,5}                   
# b ={4,5,6,7,8}

# s = a.union(b)
# print(s)


                    #        or  union ko( | )  aise bhi likha jata hai


# a ={1,2,3,4}
# b ={3,4,5,6,7}

# s =  a|b
# print(s)


# 2)                                              intersection_set

# a = {1,2,3,4,5}
# b ={4,5,6,7,8}

# s = a.intersection(b)
# print(s)



#           or   



# a = {1,2,3,4,5}
# b ={4,5,6,7,8}

# s = a&b
# print(s)



#                                         3)    diffrence_set


# a = {1,2,3,4,5}
# b ={4,5,6,7,8}

# s = b.difference(a)
# print(s)
                    #         or

# a = {1,2,3,4,5}
# b ={4,5,6,7,8}

# s = a - b
# print(s)




#                                           4) symmetric_set  

# a = {1,2,3,4,5}
# b ={4,5,6,7,8}

# s = a.symmetric_difference(b)
# print(s)   


#              or  


# a = {1,2,3,4,5}
# b ={4,5,6,7,8}

# s = a ^ b
# print(s)




# a ={1,2,3,4,5}
# b ={4,5,6,7,8}

# b -= a
# print(b)



# x = [11,22,33,22,44,55,66,77]
# l=[]
# y = int(input("enter a number : -"))
# for i in range(len(x)):
#     if(y==x[i]):
#         l.append(i)
# if(len(l)==0):
#     print("the number is not present")
# else:
#     print(l)




# x = [11,22,33]
# y =[]
# result =[]


# x ='RKU'
# Y =['R','K','U']
# result =[]

# # PRESS 1 TO DELETE STACK WISE : 1
# z =['u','k','r']


# for i in range (len(x)-1,-1,-1):
#     result.append(x[i])
# print(result) 



# for i in range(1,11):
#     if i%2 ==0:9
#         print(i)



# help(list)


# l = [12,34,555,665,45,34,55,77,994,45]

# largest =l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"your number is {largest} at index {index}")             


# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]


# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i

#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest, largest)


a = [12,13,14,15,16]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")    
