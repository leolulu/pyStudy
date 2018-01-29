i = 0
j = 1
while i < 10000:
    while j < 1000:
        if (i + 100 == j * j) and (i + 268 == j * j):
            print(i)
        #print('j=' + str(j))
        j += 1
    j = 1
    #print('i=' + str(i))
    i += 1
