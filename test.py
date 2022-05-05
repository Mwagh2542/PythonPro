##  This is First Program
print("***************FIRST PROGRAMMING**************************** \n")
str1 = "this is my first program"

print("This is First Program")
print("See here First words in Capital :     ", str1.capitalize())

print("See here all words in Capital :     ", str1.upper())

x = "Hello"
print ("\n  Here I use replace function for change any character")  
print (x.replace("H","J"))
print (x.replace("l","L"))

print("**************SECOND PROGRAMMING FOR TYPE *********************************** \n")

a = 3.58
b = "Hello"
print("This is Second Program, in this program we use type syntex \n")
print("in this program i define 2 veriables \n")
print("in First veriable I define with float \n and second define with String. \n")
print(type(a))
print(type(b))


print("**************THIRD PROGRAMMING FOR RANGE *********************************** \n")
num1 = list(range(1,11,1))
print (num1)

print("************** FORTH PROGRAMMING FOR CALCULATION with IF Condition ********************** \n")
# this use for comments

num1 = int(input("Enter the Markes in English "))
num2 = int(input("Enter the Markes in Hindi "))
total = num1 + num2
perc = (total * 100) / 200
print ("\n", "Total", total, "out of 200")
print (perc, "%")
if perc > 75:
    print("A Gread")
elif perc > 55 < 75:
    print ("B Gread")
elif perc > 35 < 55:
    print ("C Gread")
else :
    print("Try Again")
