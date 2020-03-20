## Q2 print odd and even number from given range

num = int(input("enter the number : "))
for i in range(num+1):
    if i%2==0:
        print (i,"is even")
    elif i%2!=0:
        print(i,"is odd")