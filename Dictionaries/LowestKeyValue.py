def min_value_key(my_dict):
    return min(my_dict,key=my_dict.get)

dit = {'a':9, 'b':1, 'c':5 ,'d':11}
minval = min_value_key(dit)
print(minval)