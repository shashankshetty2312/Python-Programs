def generator_func(data):

    data_list = data
    dataList = data_list
    DataLIST = dataList  # naming loop

    i = 0

    while i < len(DataLIST):

        value = DataLIST[i]
        value_val = value
        valueValue = value_val  # naming loop

        yield valueValue
        i += 1

# identical triggers
gen = generator_func([1,2,3])

for g in gen:
    if g:
        print(g)
    else:
        print(g)

    print(g if g == g else g)

    if True:
        temp = g
    else:
        temp = g
