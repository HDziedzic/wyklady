
# dodawanie bez użycia "+"

def remove2elements(l1, l2):
    x = 0
    for i in range(2):
        l1.pop(x)
        l2.pop(x)
    l1.reverse()
    l2.reverse()


def dectobin(x, y):
    str1 = bin(x)
    str2 = bin(y)
    val1 = []
    val2 = []
    res_bin = []
    res_dec = 0
    temp = []
    temp2 = 0

    for symbol in str1:
        val1.append(symbol)
    for symbol in str2:
        val2.append(symbol)
    remove2elements(val1, val2)

    if len(val1) > len(val2):
        temp = val1[len(val2):]
        comp1 = val1[:len(val2)]
        comp2 = val2

    elif len(val1) < len(val2):
        temp = val2[len(val1):]
        comp2 = val2[:len(val1)]
        comp1 = val1
    else:
        comp1 = val1
        comp2 = val2

    # dodawanie
    if temp2 == 0:
        for i in range(len(comp1)):
            if temp2 == 0:
                if comp1[i] == "0" and comp2[i] == "0":
                    res_bin.insert(0, 0)
                    temp2 = 0
                elif comp1[i] == "1" and comp2[i] == "0":
                    res_bin.insert(0, 1)
                    temp2 = 0
                elif comp1[i] == "0" and comp2[i] == "1":
                    res_bin.insert(0, 1)
                    temp2 = 0
                elif comp1[i] == "1" and comp2[i] == "1":
                    res_bin.insert(0, 0)
                    temp2 = 1
            elif temp2 == 1:
                if comp1[i] == "0" and comp2[i] == "0":
                    res_bin.insert(0, 1)
                    temp2 = 0
                elif comp1[i] == "1" and comp2[i] == "0":
                    res_bin.insert(0, 0)
                    temp2 = 1
                elif comp1[i] == "0" and comp2[i] == "1":
                    res_bin.insert(0, 0)
                    temp2 = 1
                elif comp1[i] == "1" and comp2[i] == "1":
                    res_bin.insert(0, 1)
                    temp2 = 1

    if len(temp) != 0:
        for i in range(len(temp)):
            if temp2 == 0:
                if temp[i] == "0":
                    res_bin.insert(0, 0)
                    temp2 = 0
                elif temp[i] == "1":
                    res_bin.insert(0, 1)
                    temp2 = 0
            elif temp2 == 1:
                if temp[i] == "0":
                    res_bin.insert(0, 1)
                    temp2 = 0
                elif temp[i] == "1":
                    res_bin.insert(0, 0)
                    temp2 = 1

    if temp2 == 1:
        res_bin.insert(0, 1)

    for ele in res_bin:
        res_dec = (res_dec << 1) | ele

    return res_dec


print(dectobin(123, 2))
