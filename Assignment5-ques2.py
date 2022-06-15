n= int(input("enter number: "))
a= int(input("enter minimum value: "))
b= int(input("enter maximum value: "))
for i in range(a,b):
    if(i%n==0):
        print(i)