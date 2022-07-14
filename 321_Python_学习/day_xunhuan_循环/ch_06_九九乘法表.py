row = 1
while row <= 9:
    col = 1
    while col <= row:
        jg = row *col
        # print("%d * %d = ", end=""% row ,col)
        print("%d * %d = %d" % (col, row, jg),end="\t")
        col += 1

    print("  ")
    row += 1
