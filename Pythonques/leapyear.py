#Program to find leap Year
user_input=int(input("Enter a Year: "))
output="Leap year" if user_input%400==0 else "Leap Year" if user_input%4==0 & user_input%100==0 else "Not a leap year"
print(output)
# sample
# ly=2000,2004
# nly=2015,1990