a= int(input("enter side: "))
b= int(input("enter side: "))
c= int(input("enter side: "))
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5

if(a<b+c and c<a+b and b<a+c):
    print("triangle is possible")
    print("Area:",area)
else:
    print("triangle is not possible")


