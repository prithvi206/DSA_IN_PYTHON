def merge_dicts(dict1, dict2):
    # TODO
    result = dict1.copy()
    for key , value in dict2.items():
        result[key] = result.get(key,0) + value
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
