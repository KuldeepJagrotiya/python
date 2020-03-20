# ## Q : remove the duplicates from above list
l1 = [1,4,3,4,2,4,2,1,6]
l2 = list()
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)