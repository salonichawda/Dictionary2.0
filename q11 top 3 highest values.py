my_dict = {

    'a':50, 

    'b':58, 

    'c':56,

    'd':40, 

    'e':100, 

    'f':20

    }

x=[]

dic1=sorted(my_dict.values())

x.append(dic1[-1])

x.append(dic1[-2])

x.append(dic1[-3])

print(x)






my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20}
max=0
a=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        b=i
a.append(max)
my_dict.pop(b)
secound_mx=0
for i in my_dict:
    if my_dict[i]>secound_mx:
        secound_mx=my_dict[i]
        c=i
a.append(secound_mx)
my_dict.pop(c)
third_mx=0
for i in my_dict:
    if my_dict[i]>third_mx:
        third_mx=my_dict[i]
a.append(third_mx)
print(a)




my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20}
max=0
a=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        b=i
a.append(b)
my_dict.pop(b)
secound_mx=0
for i in my_dict:
    if my_dict[i]>secound_mx:
        secound_mx=my_dict[i]
        c=i
a.append(c)
my_dict.pop(c)
third_mx=0
for i in my_dict:
    if my_dict[i]>third_mx:
        third_mx=my_dict[i]
        d=i
a.append(d)
print(a)