size=int(input("enter the size:"))

dic={}

for i in range(size):

    name=input("enter the name of students:")

    marks=int(input("enter the marks of students:"))

    dic.update({name:marks})
    
print(dic)