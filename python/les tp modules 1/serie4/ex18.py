listevide=[]
listfloattant=[0,0,0,0,0]
print(listevide)
print(listfloattant)
for i in range(0,1001):
    if i==200:
         listevide.insert(200,"step")
    listevide.append(i)
print(listevide)