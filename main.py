sl1 = [[0, 5], [0.033, 10], [0.09, 15], [0.167, 20], [0.327, 25], [0.735, 30], [0.944, 35], [1, 40], [0.868, 45], [0.508, 50], [0, 55]]
sl2 = [[0, 35], [0.3, 40], [0.6, 45], [0.83, 50], [0.944, 55], [1, 60], [0.944, 65], [0.783, 70], [0.536, 75], [0.267, 80], [0, 85]]


def sum_table():
    table = []
    for i in range(len(sl1)):
        row = []
        for j in range(len(sl2)):
            summ = sl1[j][1] + sl2[i][1]
            funkres = min(sl1[j][0], sl2[i][0])
            pair = [funkres, summ]
            row.append(pair)
        table.append(row)
    return table


def mult_table():
    table = []
    for i in range(len(sl1)):
        row = []
        for j in range(len(sl2)):
            summ = sl1[j][1] * sl2[i][1]
            funkres = min(sl1[j][0], sl2[i][0])
            pair = [funkres, summ]
            row.append(pair)
        table.append(row)
    return table


def subtr_table():
    table = []
    for i in range(len(sl1)):
        row = []
        for j in range(len(sl2)):
            summ = sl1[j][1] - sl2[i][1]
            funkres = min(sl1[j][0], sl2[i][0])
            pair = [funkres, summ]
            row.append(pair)
        table.append(row)
    return table


def div_table():
    table = []
    for i in range(len(sl1)):
        row = []
        for j in range(len(sl2)):
            summ = sl1[j][1] / sl2[i][1]
            funkres = min(sl1[j][0], sl2[i][0])
            pair = [funkres, summ]
            row.append(pair)
        table.append(row)
    return table


def addup():
    tabl = sum_table()
    i = j = 0
    result = [tabl[i][j]]
    while i < len(tabl)-1 and j < len(tabl[j])-1:
        if tabl[i][j+1][0] == tabl[i+1][j][0]:
            i += 1
            j += 1
            result.append(tabl[i][j])
        else:
            i += int(tabl[i+1][j][0] > tabl[i][j+1][0])
            j += int(tabl[i+1][j][0] < tabl[i][j+1][0])
            result.append(tabl[i][j])
    return result


def multiply():
    tabl = mult_table()
    i = j = 0
    result = [tabl[i][j]]
    while i < len(tabl)-1 and j < len(tabl[j])-1:
        if tabl[i][j+1][0] == tabl[i+1][j][0]:
            i += 1
            j += 1
            result.append(tabl[i][j])
        else:
            i += int(tabl[i+1][j][0] > tabl[i][j+1][0])
            j += int(tabl[i+1][j][0] < tabl[i][j+1][0])
            result.append(tabl[i][j])
    return result


def divide():
    tabl = div_table()
    i = len(tabl)-1
    j = 0
    result = [tabl[i][j]]
    while i > 0 and j < len(tabl[j])-1:
        if tabl[i][j+1][0] == tabl[i-1][j][0]:
            i -= 1
            j += 1
            result.append(tabl[i][j])
        else:
            i -= int(tabl[i-1][j][0] < tabl[i][j+1][0])
            j += int(tabl[i-1][j][0] > tabl[i][j+1][0])
            result.append(tabl[i][j])
    return result


def subtract():
    tabl = subtr_table()
    i = len(tabl)-1
    j = 0
    result = [tabl[i][j]]
    while i > 0 and j < len(tabl[j])-1:
        if tabl[i][j+1][0] == tabl[i-1][j][0]:
            i -= 1
            j += 1
            result.append(tabl[i][j])
        else:
            i -= int(tabl[i-1][j][0] < tabl[i][j+1][0])
            j += int(tabl[i-1][j][0] > tabl[i][j+1][0])
            result.append(tabl[i][j])
    return result




def pair_valid():
    pass


if __name__ == "__main__":
    tbl = div_table()
    for rw in tbl:
        print(rw)

    print("\n----------------------------------------\n")

    print(divide())
    #print(res)