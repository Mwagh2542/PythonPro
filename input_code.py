# in this code we Import Date-Util Module provide a class RELATIVE-DELTA, which represents an interval of time.
# The RELATIVE-DELTA class has following attributes which tells about the duration
from datetime import date

x = input (int("Enter the Name of Student : ")) # Here X is Global Veriable because it's outside of function body
born= int(1979)
def claculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    print(born)
    claculate_age()

info = help() # No argument  
# Displaying result  
print(info) 

print(list(range(5)))

# opens python.text file of the current directory  
f = open("filename.docx")
# specifying full path  
f = open("C:/Users/mwagh/Desktop/filename.docx")


print(born)
#age1 = age - age
print (x)
def sample_function():
    print("Global Value is defined out side the function-body ", x)



# SELECT DATEDIFF (
# 	year, DOB, getdate()) + CASE 
#       WHEN (DATEADD(year,DATEDIFF(year, DOB, getdate()) , DOB) > getdate())
#       THEN - 1 
#       ELSE 0
# END
# )