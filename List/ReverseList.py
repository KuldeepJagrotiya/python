# ## Q : reverse the list without using reverse functions
##M-1
l1 = [1,3,8,7,3,1,5,3]
l2 = l1[::-1]
print(l2)

##M-2
l1 =[1,3,8,7,3,1,5,3]
l2 = list()
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print(l2)