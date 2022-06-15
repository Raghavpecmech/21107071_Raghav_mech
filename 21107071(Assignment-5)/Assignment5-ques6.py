a= int(input("enter min value: "))
b= int(input("enter max value: "))
for j in [2,3,5,7]:
    print(j)
for i in range(a,b):
    if(i%2!=0 and i-1>0):
        if(i%3!=0):
            if(i%5!=0):
                if(i%7!=0):
                  print(i)

    
    
    
    