def count_word_frequency(words):
    # TODO
    dict={}
    for word in words:
           dict[word] = dict.get(word,0)+1
    return dict

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
res = count_word_frequency(words) 
print(res)