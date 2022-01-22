d={"b":8,"g":7,"d":5,"e":4,"a":1,"c":6,"f":3}

a=list(d.values())

i=0

max=a[i]

while i<len(a):

    if a[i]>max:

        max=a[i]

    i+=1   

print(max)