

def display_table(table):

    col_widths = [0] * len(table[0])
    for row in table:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    for row in table:
        row_str = ""
        for i, val in enumerate(row):
            row_str += str(val).ljust(col_widths[i] + 2)
        print(row_str)


a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

display_table(a)