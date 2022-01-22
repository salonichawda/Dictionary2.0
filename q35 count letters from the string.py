string='w3resource'
a={}
for i in string:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print(a)
