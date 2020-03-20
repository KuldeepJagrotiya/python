## Q1 count the python occurrance without using count function

s1 ='hi python hello python Byee Python'
count=0
print(s1.split(' '))
for i in s1.split(' '):
    if i.lower()=='python':
        count+=1
print('occurrance of python : ',count)
