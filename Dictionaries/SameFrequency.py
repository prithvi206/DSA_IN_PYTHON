def check_same_frequency(list1, list2):
    # TODO
    def counter_list(lst):
        counter={}
        for element in lst:
            counter[element]= counter.get(element,0)+1
        return counter
    return counter_list(list1) == counter_list(list2)
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)