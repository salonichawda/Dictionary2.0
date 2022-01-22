dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

a={}

i=0

min=dic[i]

while i<=len(dic.items()):

    if dic[i]<min:
        min=dic[i]
    b=i
a.update({b:min})
dic.pop(b,min)

for i in dic:

    if dic[i]<min:
        min=dic[i]
    c=i
a.update({c:min})
dic.pop(c,min)

for i in dic:
    if dic[i]<min:
        min=dic[i]
    d=i
a.update({d:min})
dic.pop(d,min)

for i in dic:
    if dic[i]<min:
        min=dic[i]
    e=i
a.update({e:min})
dic.pop(e,min)

for i in dic:
    if dic[i]<min:
        min=dic[i]
    f=i
a.update({f:min})
dic.pop(f,min)

print(a)
# while i>=0:
    # i-=1
    # print(dic1[i])
    # i-=1

# print(dic1)

# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original Dictionary',d)
# sorted_d=dict(sorted(d.items()))
# print(sorted_d)

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x= sorted(d.items())
# print(x)
# y = x[::-1]
# print(y)

# d = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}

# check = d.items()

# d2 = dict(sorted(check,key = lambda e: e[-1]))
# d3 = dict(sorted(check,key = lambda e: e[-1], reverse =True))
# print(d2)
# print(d3)



# a=str(input("enter the number"))

# for i in a:
#     if a[1]==2:
#         print("yes")
#     else:
#         print("no")