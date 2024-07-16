'decision making'
#types
'''
1.if condition
2.if-else condition
3.nested if condition
4.elif condition(switchcase)
'''
#1.if condition
#In python the if condition is used to execute a block of code only if a specific condition is true.
#syn:
'''
if condition:
    statement
    (block of code)
'''
#T,F
'''
if True:
    print('Hai')
if False:
    print('Hai')
'''

#bool
'''
if bool(1):
    print('bye')
if bool(0):
    print('bye')
'''

#1.
'''
if bool(0)or bool(1):
    print('bye')
'''
#2.
'''
if bool(0) and bool(1):
    print('bye')
'''
#3.
'''
n=input("enter n value:")
if n:
    print("data is present")
print("data is not present")
'''

#2.if-Else condition
#The if-else condition is used to execute one block of code if a specific condition is true and another block of code if the condition is false.
#syn:
'''
if condition:
    stmt(block of code)--->True block
else:
    stmt(block of code)--->False block
'''

#1.
'''n=input("enter n value:")
if n:
    print("data is present")
else:
    print("data is not present")
'''

#3.Nested if-else condition
#Nested if-else condition allows you to check multiple condition in a hierarchical manner.
#That means program can have if or else block inside another if or else block.   
#syn:
'''
if cond:
    stmt
    if cond:
        stmt
    else:
        stmt
    .
    .
    .
else:
    stmt
'''
#1.
'''
if True:
    print('main if')
    if True:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')
'''
#2.
'''
if False:
    print('main if')
    if False:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')
'''
#4.elif condition(elseif)
#elif condition is used to check mutiple conditions simultaneously.
#if the if condition is false the program checks the elif condition.
#if the elif condition is True the corresponding block of code is executed.
#if all the conditions are False the else block is executed.
#syn:
'''
if cond:
    stmt
elif:
    stmt---->True block
.
.
.
else:
    stmt----->False block
'''

#1.
'''
if True:
    print('A')
elif True:
    print('B')
elif True:
    print('C')
else:
    print('False')
'''
#2.
'''if False:
    print('A')
elif False:
    print('B')
elif False:
    print('C')
else:
    print('False')
'''

#PROGRAMS
#1.Write a program to check the given number is odd?
'''
n=int(input("enter n value:"))
if n%2==0:
    print("even")
else:
    print("odd")
'''

#2.Write a program to check a character is vowel or not?
'''
n=input("enter char:")
if n=='a':
    print("vowel")
elif n=='e':
    print("vowel")
elif n=='i':
    print("vowel")
elif n=='o':
    print("vowel")
elif n=='u':
    print("vowel")
else:
    print("consonent")
'''   
3
'''
n=input("enter char:")
if n in'aeiouAEIOU':
    print("vowel")
else:
    print("consonent")
'''
#3.Check whether a string is palindrome or not?
'''
string=input("enter string:")
if (string == string[::-1]):
    print("String is palindrome")
else:
    print(" String is not a palindrome")
'''
#4.Check whether a number is palindrome or not?
'''
num=input("enter number:")
if (num == num[::-1]):
    print("number is palindrome")
else:
    print(" number  is not a palindrome")

 '''   
#5.Check whether a year is leap year or not?
'''
n=int(input("enter year"))
if n%4==0:
    print("leap year")
else:
    print("Not a leap year")
'''


#6.Write a program to check whether the number is perfect square or not?
'''
n=int(input("enter a number:"))
s=n**0.5
if s*s==n:
    print(n,"is a perfect square")
else:
    print(n,"is not a perfect square")

'''
#7.Write a program to check if the given character is alphabet or number or special character?
'''
s=input("enter value:")
if s.isalpha():
    print("s is alphabet")
elif s.isnumeric():
    print("s is a number")
elif s.isalnum():
    print("s is a special character")
else:
    print("enter only one character")
'''
#8.Write a program to print Pass if marks is greater than 35 else Fail and marks is greater than 60 print First class?
'''
marks=int(input("enter marks:"))
if marks>60:
    print("First class")
elif marks>35:
    print("pass")
else:
    print("Fail")
'''
#9.Write a program to check the starting character is vowel or not?
'''
str=input("enter string:")
if str[0]in'aeiouAEIOU':
    print("vowel")
else:
    print("Noyt vowel")
'''
#10.Write a program to check if the given list has even length?
'''
s=input("enter list:").split()
if (len(s)%2==0):
    print("Even length:")
else:
    print("odd length")
'''
#11.Write a program to check the number of keys in the dictionary if number is even print as it is otherwise add a new key to make it even and print it?
'''
dict={'a':1,'b':4,'c':6}
if len(dict)%2==0:
    print(dict)
else:
    key=input("enter a key")
    value=input("enter a value")
    dict[key]=value
    print(dict)
'''
#Task-1
#12.Write a program to check whether first number is even or odd?
'''
n=int(input("enter number:"))
if n[0]%2==0:
    print("even")
else:
    print("odd")
'''
#13.Write a program to check whether second last number is even or odd?
'''
n=(input("enter n value:"))
second_last=int(n[-2])
if (second_last)%2==0:
      print("even number")
else:
    print("odd number")
'''


'''
n=int(input("enter n value:"))
n_str=str(n)
second_last=int(n_str[-2])
if (second_last)%2==0:
      print("even number")
else:
    print("odd number")
'''

#14.Write a program to check if the given data type is string datatype?
'''
a="rani"
if isinstance(a,str):
    print("string")
else:
    print("not string")
'''
#15.Write a program to check largest number in user input?
'''
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
if n1>=n2 and n1>=n3:
    print("n1 is greatest")
elif n2>=n1 and n2>=n3:
    print("n2 is greatest")
else:
    print("n3 is greatest")
'''
#16.Write a program to check if the given data type is float?
'''
a=1.7
if isinstance(a,float):
    print("float")
else:
    print("not float")
'''
#17.write a program to check list is empty or not?
'''
l=input("enter the numers into list:")
l1=list(l)
if len(l1)==0:
    print("empty list")
else:
    print("list is not empty")
'''
#18.write a program to return the length of string if characters are present?
'''
s=input("enter string:")
if len(s)==0:
    print("string is not given")
else:
    print(len(s))
'''
#19.write a program  to get the last element in list?
'''
l=input("enter values into list:")
l1=list(l)
if len(l1)==0:
    print("list is empty")
else:
    print(l1[-2])
'''
#20.write a program to get middle character in string?
'''
str=input("enter string: ")
x=len(str)
y=x//2
print("the middle character is:str[y]")
'''
#21.Write a program to check the given data is number or special character?
'''
v=int(input("enter value:"))
if ((v>=32 and v<=47) or (v>=58 and v<=64) or (v>=91 or v<=96) and (v>=123 and v<=126)):
    print("special character")
else:
    print("number")
'''
#22.write a program to check whether the given integer is positive or negative?
'''
n=int(input("enter a number:"))
if n>0:
    print("positive")
else:
    print("negative")
'''
#23.write a program to check smallest number from user input?
'''
n1=input("enter value1:")
n2=input("enter value2:")
n3=input("enter value3:")
if n1<n2 and n1<n3:
    print("n1 is smallest")
elif n2<n3 and n2<n1:
    print("n2 is smallest")
else:
    print("n3 is smallest")
'''
#24.write a program to check tuple is empty or not?
'''
t=input("enter a tuple:")
t1=tuple(t)
if len(t)==0:
    print("tuple is empty")
else:
    print("tuple is not empty")
'''
#25.Write a program to check the given number is divisible by 5 or 8 or both?
'''
n=int(input("enter number:"))
if (n%5==0) and (n%8==0):
      print("divisible by 5 and 8")
elif n%5==0:
        print("divisible by 5")
elif n%8==0: 
    print("divisible by 8")
else:

   print("not divisible by 5 and 8")
'''
# 26.Construct a marksheet using elifladder?
'''
marks=int(input("enter marks:"))
if marks>=90:
    Grade='A+'
elif marks>=80:
    Grade='A'
elif marks>=70:
    Grade='B'
elif marks>=60:
    Grade='C'
elif marks>=50:
    Grade='D'
else:
    Fail
print("marks",marks)
print("Grade",Grade)
'''
#27.Write a program to check given number is prime or not?
'''
number=int(input("enter value:"))
if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number, "is not a prime number.")
            break
else:
    print(number, "is a prime number.")
'''
#28.Write a program by taking length and breadth as input of rectangle is equal print square or not?
'''
length=input("enter length of rectangle:")
breadth=input("enter breadthb of rectangle:")
if length==breadth:
    print("It is a square")
else:
    print("It is a rectangle")
'''
#Task-2
#29.Aschool has following rules for getting system
#a.beloW 25-F
#b.25 to 45-E
#c.45 to 50-D
#d.50 to 60-c
#e.60 to 80-B
#f.80 to above-A
'''
marks=int(input("enter marks:"))
if marks>80:
    Grade='A'
elif (60>=marks<=80):
    Grade='B'
elif (50>=marks<=60):
    Grade='C'
elif (45>=marks<=50):
    Grade='D'
elif (25>=marks<=45):
    Grade='E'
else:
    Grade='F'
print("marks",marks)
print("Grade",Grade)
'''
#30.Take input of age of 3 people by user and determine oldest among them?
'''
p1=int(input("enter age of first person:"))
p2=int(input("enter age of second person:"))
p3=int(input("enter age of third person:"))
if p1>=p2 and p1>=p3:
    print("First person is oldest")
elif p2>=p1 and p2>=p3:
    print("Second person is oldest")
else:
    print("Third person is oldest")
'''
#31.Take input of age of 3 people by user and determine youngest among them?
'''
p1=int(input("enter age of first person:"))
p2=int(input("enter age of second person:"))
p3=int(input("enter age of third person:"))
if p1<=p2 and p1<=p3:
    print("First person is youngest")
elif p2<=p1 and p2<=p3:
    print("Second person is youngest")
else:
    print("Third person is youngest")
'''

#32.A student will not be allowed to sit in exam if his / her attendance is less than 75
#take following input from user number of classes held number of classes attended
#and print percentage of class attended
#ids student is allowed to sit in exam or not
'''
classes_held=int(input("enter no.of classes held:"))
classes_attended=int(input("enter no.of classes attended:"))
percentage=(classes_attended/classes_held)*100
if percentage>75:
    print("You can attend exam")
else:
    print("You cann't attend the exam")
'''
#Task-3
#33.Program to write area of rectangle using user input?
'''
l=int(input("enter length:"))
b=int(input("enter breadth:"))
area=2*l*b
print("Area of rectangle is:",area)
'''
#34.Program to square a number using user input?
'''
n=int(input("enter a number:"))
square=n*n
print("square number:",square)
'''
#35.Program to add a integer and add a float?
'''
n1=input("enter an integer:")
n2=input("enter a float value:")
ans=int(n1)+float(n2)
print(ans)
'''

#36.program to print square root value?
'''
n=int(input("enter value:"))
sqrt=float(n**0.5)
print(sqrt)
'''

#37.Program to add two numbers?
'''
n1=int(input("enter number:"))
n2=int(input("enter number:"))
add_num=n1+n2
print(add_num)

'''

#38.program to print a string 10 times?
'''
s=input("enter a string:")
i=1
while(i<=10):
    print(s)
    i=i+1
'''

#39.program to combine two integer?
'''
n1=input("enter number:")
n2=input("enter number:")
print(n1+n2)
'''
#40.program to calculate area of triangle?
'''
base=int(input("enter base of triangle:"))
height=int(input("enter height of triangle:"))
area=(1/2)*(base)*(height)
print("Area of triangle is:",area)
'''
#41.program to convert kilometers to miles?
'''
k=int(input("enter kilometers:"))
k_m=k*1000
print(k_m)
'''
#42.program to convert negative number to positive number?
'''
n_num=float(input("enter a number:"))
p_num=int(abs(n_num))
print(p_num)

'''
#43.program to convert integer to float?
'''
n=input("enter a number:")
s=float(n)
print(s)
'''

#44.program to find reminder and quotient?
'''
n1=int(input("entern n1:"))
n2=int(input("enter n2:"))
q=n1//n2
r=n1%n2
print("Quotient:",q)
print("Reminder:",r)
'''

#45.program to round a number?
'''
import math
n=float(input("enter a number:"))
print(math.floor(n))
print(math.ceil(n))
'''
#46.program to find the simple intrest?
'''
P=int(input("enter principle value:"))
T=int(input("enter time period:"))
R=int(input("enter rate of intrest:"))
SI=(P*T*R)/100
print(SI)
'''

#47.program to find the compound intrest?
'''
P=int(input("enter principle value:"))
T=int(input("enter time period:"))
R=int(input("enter rate of intrest:"))
A=int(P(1+R)*T)
print(A)
'''

#Random module:
#The random module in python provides functions to generate random numbers choose random elements from a sequence and perform random sampling?
'Methods in random'
'1.randint--->It gives random mubers from a range'
#syn:
#import random
#random.randint(start-value,end-value)
'''import random
print(random.randint(1,10))
print(random.randint(50,60))
l=[4,9,7,6]
print(random.randint(0,len(l)-1))
index=random.randint(0,len(l)-1)
print(l[index],"at the index",index)
'''
'2.choice--->This method randomly choose a data from a sequence'
#syn:
#import random
#random.choice(sequence)
'''
import random
places=['MPL','PLR','TPT','TTD']
print("let's visit ", random.choice(places),":)")
'''

#Program to get tail or head?
'''
import random
num=random.randint(0,1)
if num==0:
    print("head")
else:
    print("tail")

'''
#Program to guess a number?
'''
import random
name=input("enter your name:")
print("hey",name,"let's start the game")
user_guess=int(input("enter a number: "))
computer_guess=random.choice((1,2,3,4,5,6,7,8,9,10))
if user_guess==computer_guess:
    print("you win")
elif user_guess<computer_guess:
    print("guess larger number")
elif user_guess>computer_guess:
    print("guess smaller number")
else:
    ("guess only numbers from tuple")
 '''                    

#'rock,paper,scissor'
'''import random
computer_items=random.choice(['scissor','rock','paper'])
user_input=input("scissor or rock or paper:")
if computer_items==user_input:
    print("draw")
elif computer_items=="scissor":
    if user_input == 'rock':
        print('you won rock hits scissor')
    else:
        print('you lost scissor cuts the paper')
elif computer_items =="rock":
    if user_input == 'paper':
        print('you won paper wraps the rock')
    else:
        print('you lost rock hits the scissor')
else:
    if user_input == 'scissor':
        print('you won scissor cuts the paper')
    else:
        print('you lost psaper wrap the rock')
'''
#LOOPING--->
'LOOPING IN PYTHON IS A CONCEPT THAT ALLOWS US TO EXECUTE A BLOCK OF CODE REPEATEDLY.'
#TYPES OF LOOPING:
'1.WHILE LOOP'
'2.WHILE-ELSE LOOP'
'3.FOR LOOP'
'4.FOR-ELSE LOOP'

#1.WHILE LOOP
#A WHILE LOOP IN PYTHON  REPEATEDLY EXECUTES A BLOCK OF CODE AS LONG AS A GIVEN CONDITION IS TRUE.
#syn:
#'INITIALIZE'
#'WHILE CON:'
#    'BLOCK OF CODE'
 #   'INCREMENT/DECREMENT'
#examples

 
#1.Write a program to print the numbers from 1 to 5?
'''
i=1
while(i<=5):
    print(i)
    i=i+1
'''

#2.Write a program to print 5 to 1?
'''    
i=5
while(i>=1):
    print(i)
    i=i-1
'''

#3.Write a program to print banglore 10 times?

'''
i=1
while(i<=10):
    print('banglore',i)
    i+=1
'''

#4.Write a program to print your name n times?
'''
name=input("enter your name:")
n=int(input("enter n:"))
i=1
while(i<=n):
    print(name,i)
    i+=1
'''

#5.Write a program to square the numbers from start and end?
'''
n1=int(input("enter start value:"))
n2=int(input("enter end value:"))
i=1
while(n1<=i<=n2):
    print(i*i)
    i=i+1
'''
'''
n1=int(input("enter start value:"))
n2=int(input("enter end value:"))
while(n1<=n2):
    print(n1*n1)
    n1+=1
'''
'''
#'with method-->append'
n1=int(input("enter start value:"))
n2=int(input("enter end value:"))
l=[]
while(n1<=n2):
    l.append(n1*n1)
    n1+=1
print(l)
'''
#'without method-->+'
#list+list
'''
n1=int(input("enter start value:"))
n2=int(input("enter end value:"))
l=[]
while(n1<=n2):
    l=l+[n1*n1]
    n1+=1
print(l)
'''

#6.Write a program to get the character and its indexes?
'''
s=input("enter a string:")
index=0
j=len(s)
while(index<len(s)):
    print(index,s[index])
    index+=1
'''

#'pack as tuples'
'''
s=input("enter a string:")
index=0
l=[]
while(index<len(s)):
    l.append([(index,s[index])])
    index+=1
print(l)
'''
#7.Program to print nested list with character and its ascii value?
'''
s=input("enter a string:")
index=0
l=[]
while(index<len(s)):
    l.append([s[index],ord(s[index])])
    index+=1
print(l)
'''

#8.program to get element and its length take the input from user?
''''
n=input("enter number:").split()
i=0
while (i<len(n)):
    n=n[i]
    
    print([n,len(n)])
    
'''   
#9.program to get the numbers starting with even?
'''
numbers=[2,3,4,45,43,29,12,90,77,65]
i=0
while i<len(numbers):
    if int(str(numbers[i][0])%2==0:
           print(numbers[i])
    i+=1
'''
#10.program to convert lowercase to uppercase?
'''
s=input("enter string in lowercase:")
if s.islower():
    print(s.upper())
'''
#11.program to convert uppercase to lowercase?
'''
s=input("enter string in lowercase:")
if s.isupper():
    print(s.lower())
'''

#12.program to convert uppercase to lowercase and lowercase to uppercase with method?
'''
s=input("enter string :")
if s.isupper():
    print(s.lower())
else:
    print(s.upper())

'''
#13.program to convert uppercase to lowercase and lowercase to uppercase without method?
'''
s=input("enter:")
if 'a'<=s<='z':
    print(ord(s))
    print(ord(s)-32)
    print(chr(ord(s)-32))
elif 'A'<=s<='Z':
    print(ord(s))
    print(ord(s)+32)
    print(chr(ord(s)+32))
else:
    print("It's not a character")
        
'''

#14.program to convert uppercase to lowercase and lowercase to uppercase without using method?
'''
s=input("enter:")
index=0
new_s=''
while index<len(s):
    if 'a'<=s[index]<='z':
        new_s+=chr(ord(s[index])-32)
    elif 'A'<=s[index]<='Z':
         new_s+=chr(ord(s[index])+32)
    else:
        new_s+=s[index]
    index+=1
print(new_s)
'''
#15.program to print to get string in reverse order?
'''
inp=input("enter string:")
i=0
n_s=' '
while i<len(inp):
    n_s=inp[i]+n_s
    i+=1
print(n_s)
'''
#16.program to print indexes and characters  of a string?
'''
s=input("enter a  string:")
i=0
while i<len(s):
    print(i,s[i])
    i+=1
'''
#17.program to get the length of string in a list?
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
i=0
length=[]
while i<len(names):
    length.append(len(names[i]))
    i+=1
print(length)
'''
#18.program to get the 1st character of each string in list?
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
i=0
list=[]
while i<len(names):
    list.append(names[i][0])
    i+=1
print(list)
'''
#19.program to get the end character of each string in list?
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
i=0
list=[]
while i<len(names):
    list.append(names[i][-1])
    i+=1
print(list)
'''

#20.create a dictionary with starting character and word in the list?
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
dic={}
i=0
while i<len(names):
    dic[names[i][0]]=names[i]
    i+=1
print(dic)

'''

#21.create a dictionary with word and lengthword in the list?
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
dic={}
i=0
while i<len(names):
    dic[names[i]]=len(names[i])
    i+=1
print(dic)
'''

#22.Program to get factorial of a number?
'''
n=int(input("enter number:"))
i=1
fact=1
while n>=i:
    fact=fact*i
    i+=1
print("factorial of n is:",fact)
'''

#23.Program to print only the words starting with vowel?
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
i=0
while i<len(names):
    if (names[i][0]).lower() in('a','e','i','o','u'):
        print(names[i])
        i+=1
'''
#program to get the numbers which is of even?
'''
l = [2, 3, 4, 45, 43, 89, 12, 90, 77, 65]
i=0
e_n=[]
while i<len(l):
    if l[i]%2==0:
        e_n.append(l[i])
    i+=1
print(e_n)
        
'''


#program to get the numbers starting with even number?
'''
l=[2, 3, 4, 45, 43, 89, 12, 90, 77, 65, 34, 234, 89, 45, 620]
i=0
s_en=[]
while i<len(l):
    if str(l[i])[0]in['2','4','6','8']:
        s_en.append(l[i])
    i+=1
print(s_en)
'''

#program to get the numbers ending with odd number?
'''
l=[2, 3, 4, 45, 43, 89, 12, 90, 77, 65, 34, 234, 89, 45, 620]
i=0
s_on=[]
while i<len(l):
    if str(l[i])[-1]in['1','3','5','7','9']:
        s_on.append(l[i])
    i+=1
print(s_on)
'''
#program to get 1 to 10?
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
#program to get -1 to -10?
'''
i=-1
while i>=-10:
    print(i)
    i-=1
'''
#program to get 10 to 1?
'''
i=10
while i>=1:
    print(i)
    i-=1
'''
#program to get 1 to user input?

#program to get -20 to -10?
'''
i=-20
while i<=-10:
    print(i)
    i+=1
'''
#program to get 1 to -10?
'''
i=1
while i>=-10:
    print(i)
    i-=1
'''
#program to get -1 to 20?
'''
i=-1
while i<=20:
    print(i)
    i+=1
'''
#program to get -10 to -1?
'''
i=-10
while i<=-1:
    print(i)
    i+=1
'''

#Building a dictionary of word and length pair?
'''
s="this is a bunch of words"
words=s.split()
w=dict()
i=0
while i<len(words):
    w[words[i]]=len(words[i])
    i+=1
print(w)
'''
#Flipping keys and values of the dictionary?
'''
dic={'a':1,'b':4,'c':8}
items=dic.items()
items_list=list(items)
print(items_list)
d={}
i=0
while i<len(items_list):
    d[items_list[i][1]]=items_list[i][0]
    i+=1
print(d)
'''
#program to count the number of each characters in a string?
'''
str="Guido Vann Rossum"
d=dict()
i=0
while i<len(str):
    d[str[i]]=str.count(str[i])
    i+=1
print(d)
'''
#Program to create a dictionary with word and it's count?
'''
str="Hello Welcome to Python hello hi world welcome to java"
s=str.split()
d=dict()
i=0
while i<len(s):
    d[s[i]]=str.count(s[i])
    i+=1
print(d)
'''
#dic of character and ascii value pair?
'''
s="absABS"
d=dict()
i=0
while i<len(s):
    d[s[i]]=ord(s[i])
    i+=1
print(d)
'''
#Building a dictionary whose price value is more than 200?
'''
prices={"AEMC":24.45,"APAL":612.45,"JBN":200.45,"HP":37.80,"FB":10.75}
prices_tuple=tuple(prices.items())
dic={}
i=0
while i<len(prices_tuple):
    if prices_tuple[i][1]>200:
        dic[prices_tuple[i][0]]=prices_tuple[i][1]
    i+=1
print(dic)
'''

#program to get all the alphabets from the string?
'''
s="herdsin34@hfdr"
i=0
while i<len(s):
    if s[i].isalpha():
        print(s[i])
    i+=1
'''
#program to get all the special characters in a string?
'''
s="her%dsin$34@hfdr"
i=0
while i<len(s):
    if not s[i].isalnum():
        print(s[i])
    i+=1
    
'''
#data=["hi","hello",10,"12.3",12,19,6.2]
#program to get only integers from the list?
'''
data=["hi","hello",10,"12.3",12,19,6.2]
i=0
while i<len(data):
    if type(data[i]) == int:
        print(data[i])
    i+=1
'''
'2'
'''
data=["hi","hello",10,"12.3",12,19,6.2]
i=0
while i<len(data):
    if isinstance(data[i],int):
        print(data[i])
    i+=1
'''

#program to print only vowels in a string?
'''
s="python selenium"
i=0
empty_s=''
while i<len(s):
         if s[i] in 'AEIOUaeiou':
             empty_s = empty_s+s[i]
         i+=1
print(empty_s)
         
'''



#program to get only alphanumeric characters from a sting?
'''
s="herdsin34@hfdr"
i=0
while i<len(s):
    if s[i].isalnum():
        print(s[i])
    i+=1

'''


#write a program to check if the given list of strings which is palindrome?
'''
n=input("enter elements:").split()
i=0
l=[]
while i<len(n):
    if n[i] == n[i][::-1]:
        l+=[n[i]]
    i+=1
print(l)
'''

#replace all the vowels with '*' in the string "hello world"?
'''
s="hello world"
i=0
empty_s=''
while i<len(s):
         if s[i] in 'AEIOUaeiou':
             empty_s = empty_s+'*'
         else:
             empty_s = empty_s+s[i]
         i+=1
print(empty_s)
'''             



















    







    


