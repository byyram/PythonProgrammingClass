for i in range(1, 20):
    for j in range(1, 20):
        ii = i**2
        jj = j**2

        c_squared = ii + jj

        c = c_squared**0.5
        integer = c % 1
        if integer == 0:
            print(i, j, c)
