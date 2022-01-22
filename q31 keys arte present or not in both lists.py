dict_one = {'key1': 1, 'key2': 3, 'key3': 2}

dict_two = {'key1': 1, 'key2': 2}

for key in (dict_one.keys() & dict_two.keys()):

    print(key, 'key is present in both lists')

for key,value in (dict_one.items() & dict_two.items()):

    print(key,value, 'key is present in both lists')
