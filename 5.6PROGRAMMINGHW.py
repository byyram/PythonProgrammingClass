def rotate(argu1, argu2, argu3):
    tuple_1 = (argu2, argu3, argu1)
    return tuple_1
a, b, c = 'Doug', 22, 1984

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)
