## Q2 find the index of 'python" in below string

s ='hi python hello python Byee Python'
for i in range(len(s)):
    if s[i:i+6]=='python':
        print("index of python is : ",i)
        break