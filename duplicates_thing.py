def duplicateChars(word):

    dictRepeats = {}

    for el in word:
        if el in dictRepeats:
            dictRepeats[el] += 1
        else:
            dictRepeats[el] = 1
    

    elements_repeated = 0

    for el in dictRepeats:
        if dictRepeats[el] == 1:
            pass
        else:
            elements_repeated += 1
    
    return elements_repeated

print(duplicateChars("indivisibility"))