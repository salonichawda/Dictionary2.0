dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
d={}
for i in dic2:
    if i in dic1:
        dic1[i]+=dic2[i]
        dic4.update(dic1)
    else:
        dic1[i]=dic2[i]
        dic4.update(dic1)
for i in dic4:
    if i in dic3:
        dic3[i]+=dic4[i]

        d.update(dic3)
    else:
        dic3[i]=dic4[i]
        d.update(dic3)
dic4.update(d)

print(dic4)