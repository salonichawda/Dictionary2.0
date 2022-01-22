a={'s  001':23,'s  01':22}
b={}
for k,v in a.items():
    
    a=({k.replace(" ", ""):v})

    b.update(a)
    
print(b)
