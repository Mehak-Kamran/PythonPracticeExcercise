''' Write a program to iterate the first 10 numbers, and in each iteration, print the sum 
    of the current and previous number.
'''

nos=int(input("Enter a number"))
#used for iterating integers
print("Printing current no and previous no in range(",nos,")")
prev=0
for no in range(nos+1):
    sum=prev+no
    print("Current no is",no,"Previous no is",prev,"and their sum is",sum)
    prev=no
    