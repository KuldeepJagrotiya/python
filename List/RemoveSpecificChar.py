# ## Q : remove 4 without using remove function
l1 = [1,2,3,4,5,4,6,4]
l2 =list()
for i in l1:
    if i!=4:
        l2.append(i)
print(l2)