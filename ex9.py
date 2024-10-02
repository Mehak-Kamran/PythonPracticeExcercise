#Write a program to check if the given number is a palindrome number.

number=input("Enter a number: ")
rev_num=number[::-1]
print(rev_num)
if number==rev_num:
    print("Number is Palindrome")
else:
    print("Number is not a palindrome")
