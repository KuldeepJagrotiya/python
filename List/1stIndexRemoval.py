# ## Q: print list and remove 1st index value untill their is no value at index 1
l1 = [1,3,8,7,3,1,5,3]  
while(len(l1)>=2):
    l1.pop(1)
print(l1)