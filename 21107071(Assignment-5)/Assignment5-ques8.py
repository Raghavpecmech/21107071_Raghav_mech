n=10
list=[]
count=0
for i in range(n):
    integer=int(input("enter integer: "))
    list.append(integer)
print(list)

#a
for i in list:
    if(i>0):
        print(i)
        count+=1
print("Number of times each number occurs in the List:",count)

#b
for i in list:
    if(i<0):
        print(i)
        count+=1
print("Number of times each number occurs in the List:",count)

#c
for i in list:
    if(i%2!=0):
        print(i)
        count+=1
print("Number of times each number occurs in the List:",count)

#d
for i in list:
    if(i%2==0):
        print(i)
        count+=1
print("Number of times each number occurs in the List:",count)
