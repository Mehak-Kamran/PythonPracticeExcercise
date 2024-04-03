#Write a program to check if the given number is a palindrome number.

number=input("Enter a number: ")
rev_num=number[::-1]
print(rev_num)
if number==rev_num:
    print("No is Palindrome")
else:
    print("No is not a palindrome")