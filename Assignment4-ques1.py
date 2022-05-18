n= int(input("Enter marks: "))
if(n>80):
    print("A")
elif(60<=n<=80):
    print("B")
elif(50<=n<60):
    print("C")
elif(45<=n<50):
    print("D")
elif(25<=n<45):
    print("E")
elif(n<25):
    print("F")
else:
    print("invalid grade")