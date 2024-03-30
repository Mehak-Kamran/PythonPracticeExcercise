'''Write a program to accept a string from the user and display 
   characters that are present at an even index number.
'''

userstr=input("Enter a string: ")
print("Printing only the even indexes:")
userstr=list(userstr)
#used to iterate list
for i in userstr[::2]:
    print(i)
   
    