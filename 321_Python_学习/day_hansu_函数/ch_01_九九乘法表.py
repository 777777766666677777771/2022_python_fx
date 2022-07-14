def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            jg = row * col
            # print("%d * %d = ", end=""% row ,col)
            print("%d * %d = %d" % (col, row, jg), end="\t\t")
            col += 1

        print("  ")
        row += 1
# multiple_table()