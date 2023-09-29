def duplicateChars(word):

    dictRepets = {}

    for el in word:
        if el in dictRepets:
            dictRepets[el] += 1
        else:
            dictRepets[el] = 1
    
    new_dict = {}
    elements_repeated = 0

    for el in dictRepets:
        if dictRepets[el] == 1:
            pass
        else:
            new_dict[el] = dictRepets[el]
            elements_repeated += 1
    
    return elements_repeated

print(duplicateChars("indivisibility"))