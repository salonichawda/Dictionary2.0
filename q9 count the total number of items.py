dict =  {

   'Alex': ['subj1', 'subj2', 'subj3'], 

   'David': ['subj1', 'subj2']}

count=0

for i in dict.values():
    
    for j in range(len(i)):
    
        count+=1

print(count)



dict =  {

   'Alex': ['subj1', 'subj2', 'subj3'], 

   'David': ['subj1', 'subj2']}

count=0

for i in dict:
    
    for j in dict[i]:
    
        count+=1

print(count)