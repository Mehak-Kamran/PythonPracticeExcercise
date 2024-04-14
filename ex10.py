'''Write a program to print N prime NUmbers till N.'''

input_no=int(input())
i=2
for i in range(i,input_no+1):
    if(i%2==0):
        i+=1
    else:
        print(i)
        i+=1
