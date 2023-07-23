def max_value_key(my_dict):
    # TODO
    return max(my_dict , key=my_dict.get)

dit = {'a':9, 'b':1, 'c':5 ,'d':11}
maxval = max_value_key(dit)
print(maxval)