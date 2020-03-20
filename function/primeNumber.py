# Q1 take the input from user and  print the prime number in the given the range

num = int(input("enter the number : "))
for i in range(1,num+1):
    for j in range(1,i):
        if (i%j==0 and j!=1):
            # print("number is not prime")
            break
    else:
        print(i,"is a prime number")