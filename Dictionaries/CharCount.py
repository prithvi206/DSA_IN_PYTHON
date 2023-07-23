def charCount(strn):
    result = {}

    for i in strn.lower():
        if isinstance(i,str) and not(i.isspace()):
            result[i] = result.get(i,0)+1
    return result
print(charCount("My name is Elshad"))
    
