dic1={"a":100,"b":200,"c":300}

dic2={"a":200,"b":200,"d":400}

for i in dic2:

    if i in dic1:
    
        dic1[i]+=dic2[i]
    
    else:
    
        dic1[i]=dic2[i]

print(dic1)
    