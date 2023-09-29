
def checksum(cardnum):
    cardnum = str(cardnum)

    cardnum = list(cardnum)
    cardnum = reversed(cardnum)

    one_or_two = 2

    mult_list = []

    for el in cardnum:
        if one_or_two == 2:
            mult_list.append(int(el) * 2)
            one_or_two = 1
        else:
            mult_list.append(int(el) * 1)
            one_or_two = 2

    sum_dig = []

    for el in mult_list:
        if el >= 10:
            el_split = [int(digit) for digit in str(el)]
            sum_number = sum(el_split)
            sum_dig.append(sum_number)
        else:
            sum_dig.append(el)

    sum_result = sum(sum_dig)
    checksum = (sum_result // 10 + 1) * 10
    result = checksum - sum_result

    print(result%10)

checksum(491748458989710)
checksum(62)

#full card number = 4917484589897107
#full card number = 62