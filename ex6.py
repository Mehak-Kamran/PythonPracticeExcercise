#Iterate the given list of numbers and print only those numbers which are divisible by 5

no=5
input_list=[]
div_list=[]
for _ in range(0,no):
    val=int(input("Enter a no: "))
    input_list.append(val)
for index in input_list:
        if index%5==0:
            div_list.append(index)
        else:
            pass

print("Original List", input_list)
print("Divisible by 5: ",div_list)

