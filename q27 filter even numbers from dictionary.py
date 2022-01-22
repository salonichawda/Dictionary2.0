d={'V':[1,4,6,10],'VI':[1,4,12],'VII':[1,3,8]}

x=[]
y=[]
z=[]
l={}
for i in d['V']:
    if i%2==0:
        x.append(i)
for j in d['VI']:
    if j%2==0:
        y.append(j)
for k in d['VII']:
    if k%2==0:
        z.append(k)
l.update({'V':x,'VI':y,'VII':z})
print(l)


