def rec_sum(els):
    if len(els) == 1:
        return els[0]
    else:
        return els[0] + rec_sum(els[1:])

print(rec_sum([1, 2, 3, 4, 5]))