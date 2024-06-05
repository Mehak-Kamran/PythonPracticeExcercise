# remove duplicate from list 
fruit_list=[]
no=int(input("Enter no of fruits "))
for i in range(no):
    print("Enter Fruits: ")
    fruit_list.append(input())
print(fruit_list)
#converst fruitlist into fruitset
fruit_set=set(fruit_list)
for fruit in fruit_set:
    print(fruit)