n = int(input("Enter a number: ")) 
sum = 0
for i in range(1, n):
    if(n % i == 0): sum = sum + i
if (sum == n):
        print(" %d is a Perfect Number" %n)
else:
    print(" %d is not a Perfect Number" %n)
