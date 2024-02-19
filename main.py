#Data Types
#String    
#print("Hello"[4])
#print("123" + "345")
#Integer
#print(123 + 345)
#123_456_789
#Float
#3.14159
#Boolean
#True
#False
# f_strings used to concatenate different data types

# convertion of differnt datatypes
str() #convert to string
int() #convert to integer
float() # convert float

# add two digit number
two_digit_number = input("Enter two dit number :")
type(two_digit_number) #check datatype
a = two_digit_number[0]
b = two_digit_number[1]

print(int(a) + int(b))

# BMI operations
height = input("Enter your height in m :")
weight = input("Enter your weight in kg :")

bmi = int(weight) / float(height) ** 2
bmi_results = round(bmi,2)
print(bmi_results)

# weeks,days and months
age = input("Enter tour age :")
age_left =90 - int(age)
message = f"You have {age_left * 352} days, {age_left * 52} weeks, and {age_left * 12} months left."
print(message)

# Tip calculator
print("Welcome to the tip calculator.")
bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_tip = float((tip / 100) + 1+bill)
people = int(input("How many people to split the bill? "))
message = f"Each person should pay: ${round(bill_tip / people,2)}"
print(message)