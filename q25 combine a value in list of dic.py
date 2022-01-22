L = [{'item': 'item1', 'amount': 400}, 

    {'item': 'item2', 'amount': 300}, 

    {'item': 'item1', 'amount': 750}]

d = {}

for i in L:

    key = i['item']

    value = i['amount']

    if key not in d.keys():

        a = {key:value}

        d.update(a)

    else:

        d[key] += value

print(d)