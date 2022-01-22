my_dict={'a':[2,3,5],

        'b':[1,8,4],

        'c':[9,0,1]}

sum=0

sum1=0

sum2=0

d={}
    
for i in my_dict['a']:
    
    sum+=i

for j in my_dict['b']:

    sum1+=j

for k in my_dict['c']:

    sum2+=k

d.update({'a':sum,'b':sum1,'c':sum2})

print(d)


