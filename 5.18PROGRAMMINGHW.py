oneten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = sum(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, oneten)))

print(total)

new_list = []

for i in range(len(oneten)):
    if oneten[i] % 2 == 0:
        new_list.append(oneten[i]*3)

print(sum(new_list))

