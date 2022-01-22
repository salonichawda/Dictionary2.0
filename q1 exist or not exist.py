# my_dict={"name":"Raju",

#         "marks":56}
        
# print(my_dict["name"])


# a=['saloni','jyoti','aadityaa','sheetal']
# b=sorted(a)
# print(b)




# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# d={}
# for i in dic2:
#     if i in dic1:
#         dic1[i]+=dic2[i]
#         dic4.update(dic1)
#     else:
#         dic1[i]=dic2[i]
#         dic4.update(dic1)
# for i in dic4:
#     if i in dic3:
#         dic3[i]+=dic4[i]

#         d.update(dic3)
#     else:
#         dic3[i]=dic4[i]
#         d.update(dic3)
# dic4.update(d)

# print(dic4)




# for i in dic1:
#         if i in dic2:
#             if dic1[i]==dic2[i]:
#                 dic1[i]+=dic2[i]
#             else:
#                 dic1[i]+=dic2[i]
# dic1.update(dic3)
# print(dic1)






dict1={'name':'Raju', 'marks':56}

i=input('enter the keys:')

if i in dict1:

    print('exit')

else:
    print('not exit')






# my_dict = { 'data1':100,  'data2': -54, 'data3': 247  }

# sum=0

# for i in my_dict.values():

#     sum+=i

# print(sum)






# Dic= {1: 'NAVGURUKUL',2: 'IN', 
#      3:{'A' : 'WELCOME',
#     'B' : 'To', 
#     'C' : 'DHARAMSALA'}}

# del Dic[3]['A']

# print(Dic)





# list1=['one','two','three','four','five']

# list2=[1,2,3,4,5]

# dic={}

# for i in range(len(list1)):

#     dic.update({list1[i]:list2[i]})

# print(dic)





# dic={
#     'ball':'red',
#     'bat':4,
#     'wickets':8,
#     'ball':'green',
#     'bat':3}
# a={}
# for i,x in dic.items():
#     if i not in a.keys():
#         a.update({i:x})
#     else:
#         a.update({i:x})
# print(a)



# list1=[
#     {"first":"1"}, 
#     {"second": "2"}, 
#     {"third": "1"}, 
#     {"four": "5"}, 
#     {"five":"5"}, 
#     {"six":"9"},
#     {"seven":"7"}]
# a=[]
# for i in range(len(list1)):
#     for j in list1[i]:
#         if list1[i][j] not in a:
#             a.append(list1[i][j])
# print(a)


# size=int(input('enter the number of students:'))
# dic1={}
# for i in range(size):
#     students=input('enter the name:')
#     marks=int(input('enter the marks:'))
#     dic1.update({students:marks})
# print(dic1)


# word="MISSISSIPPI"

# a={}

# for i in word:
#     if i not in a:
#         a[i]=1
#     else:
#         a[i]+=1
# print(a)



# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# count=0
# for i in dict1:
#     for j in dict1[i]:
#         count+=1
# print(count)


# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20}
# max=0
# a=[]
# for i in my_dict:
#     if my_dict[i]>max:
#         max=my_dict[i]
#         b=i
# a.append(max)
# my_dict.pop(b)
# secound_mx=0
# for i in my_dict:
#     if my_dict[i]>secound_mx:
#         secound_mx=my_dict[i]
#         c=i
# a.append(secound_mx)
# my_dict.pop(c)
# third_mx=0
# for i in my_dict:
#     if my_dict[i]>third_mx:
#         third_mx=my_dict[i]
# a.append(third_mx)
# print(a)



# i=1
# dic={}
# while i<=15:
#     sqr=i**2
#     dic.update({i:sqr})
#     i+=1
# print(dic)


# a="hellow   my   name is saloni chawda"

# # print(a.replace(" ", ""))
# b=""
# for i in a:
#     if i!=" ":
#         b+=i
# print(b)


# a={'s  001':23,'s  01':22}
# b={}
# for k,v in a.items():
    
#     a=({k.replace(" ", ""):v})
#     b.update(a)
# print(b)



# dic={"one":1,"two":2,"three":3,"four":4,"five":5}

# a=[]
# b=[]

# for k,v in dic.items():
#     a.append(k)
#     b.append(v)
# print(a)
# print(b)


# dic1={"a":100,"b":200,"c":300}

# dic2={"a":200,"b":200,"d":400}

# for i in dic2:
#     if i in dic1:
#         dic1[i]+=dic2[i]
#     else:
#         dic1[i]=dic2[i]
# print(dic1)



# dic1={1:10,2:20}

# dic2={3:30,4:40}

# dic3={5:50,6:60}

# dic1.update(dic2)

# dic1.update(dic3)

# print(dic1)



# dic={"red":1,"green":2,"blue":3}

# for i,j in dic.items():
#     print(i,"-",j)

    

# dic1={"a":2,"b":5,"c":8,"d":9,"e":3}
# mult=1
# for i in dic1:
#     mult*=dic1[i]
# print(mult)



# dic1={"a":2,"b":5,"c":8,"d":9,"e":3}

# key=input('enter the key:')

# if key in dic1:
    
#     dic1.pop(key)

# print(dic1)



# d={"b":8,"g":7,"d":5,"e":4,"a":1,"c":6,"f":3}

# print(sorted(d.keys()))


# d={"b":8,"g":7,"d":5,"e":4,"a":1,"c":6,"f":3}
# max=0
# for i in d:
#     if d[i]>max:
#         max=d[i]
#         a=i
# print({a:max})



# d={}

# if len(d)==0:
#     print('empty')
# else:
#     print('not empty')




# dic = {'1':['a','b'], '2':['c','d']} 

# for x in dic['1']:
#     for y in dic['2']:
#         a=x+y
#         print(a)



# list1=[1,2,3,4,5]

# d=a={}

# for i in list1:
#     a[i]={}
#     a=a[i]
# print(d)



# dic=[{1:{'a':2,'b':3},2:{'d':4,'e':5}}]

# for i in dic:
#     for j in i[2]:
#         print(j['e'])



