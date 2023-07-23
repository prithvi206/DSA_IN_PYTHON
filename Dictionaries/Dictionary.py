#Creating Dictionary

my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

eng_sp = dict(one='uno',two='dos',three='trees')
print(eng_sp)
eng_sp2 = {'one':'uno','two':'dos','three':'trees'}
print(eng_sp2)
eng_sp3 = [('one','uno'),('two','dos')]
eng_sp3 = dict(eng_sp3)
eng_sp2['four']= 'four'
print(eng_sp2)

def traversal(dict):
    for key in dict:
        print(key ,dict[key])

traversal(eng_sp2)

def Search(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return "value does not exist" 

print(Search(eng_sp2,'dos'))

removed_value = eng_sp2.pop('two',None)
print(removed_value)
eng_sp2.clear()
eng_sp4 = eng_sp2.copy()
new_Dict = {}.fromkeys([1,2,3],0)
print(new_Dict)
new_Dict.get(1,0)
eng_sp2.update(eng_sp3)

dit = {'a':9, 'b':1, 'c':5 ,'d':11}
print(sorted(dit.values()))