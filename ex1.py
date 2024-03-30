'''Given two integer numbers, return their product only if the product is equal to or lower 
than 1000. Otherwise, return their sum'''


def fun(num1,num2):
    product=num1*num2
    sum=num1+num2
    if product<=1000:
        return product
    else:
        return sum

number1=input("Enter first integer: ")
number2=input("Enter second integer: ")
if (number1 and number2).isdigit():
    number1=int(number1)
    number2=int(number2)
    result=fun(number1,number2)
    print(result)
else:
    print("Please enter a valid integer value")

    