dic1={"a":2,"b":5,"c":8,"d":9,"e":3}

key=input("enter the key:")

if key in dic1:

    del dic1[key]

print(dic1)



# a=[10,20,20,30,11,13]

# x=[]
# i=0
# while i<len(a):
#     if a[i] not in x:
#         x.append(a[i])
#     # else:
#     #     x.append(i)
#     i+=1
# print(x)

# d={"C1":[1,2,3],"C2":[5,6,7],"C3":[9,10,11]}

# print(d.keys())

# a=list(d.values())

# for i in range(len(a)):
#     print(a[i])

# for i in d.keys():
#     print(i)
#     for j in d.values():
#         for x in range(len(j)):

#             print(j[x],end="")
#         x+=1
#         print()
#             # break
