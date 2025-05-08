
def no_doubles(listing):
    newlisting = []
    for item in listing:
        if item not in newlisting:
            newlisting.append(item)
    newlisting.sort()
    return newlisting
print(no_doubles([0, 9, 7, 4, 6, 6, 9, 7, 5]))