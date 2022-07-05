def isPalindrome(s):
    return s == s[::-1]

input_string= str(input("enter word: "))
ans = isPalindrome(input_string)
 
if ans:
    print("Yes")
else:
    print("No")