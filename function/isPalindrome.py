## Q3 take the input from user and check if number is palindrome

inp = (input("enter the number : "))
out = str()
for i in range(len(inp)-1,-1,-1):
     out+=inp[i]
if out==inp:
    print(inp,"is a palindrome")
else:
    print(inp,"is not a palindrome")