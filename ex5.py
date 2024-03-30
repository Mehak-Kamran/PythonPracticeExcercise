#Write a function to return True if the first and last number of a given list is same. 
#If numbers are different then return False.

def match(list):
    
    if list[0]==list[list_length-1]:
        return True
    else:
        return False
        



list_length=int(input("Enter size of list "))
user_list=[]
for i in range(list_length):
    inputvalue=input("Enter a no:")
    user_list.append(inputvalue)

print("Given list is:",user_list)
result=match(user_list)
print(result)

