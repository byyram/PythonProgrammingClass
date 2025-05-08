x = int(input("Please give me a 5 digit number: "))

if 10000 <= x <= 100000:
    first = x / 10000
    first_remainder = (x % 10000) * 0.00001
    one = first - first_remainder
    print(one, first_remainder, first)
    print(7%3)
    x = x - first

    second = x / 1000
    second_remainder = x % 1000
    two = second - second_remainder
    x = x - second

    third = x / 1000
    third_remainder = x % 100
    three = third - third_remainder
    x = x - third

    fourth = x / 10
    fourth_remainder = x % 10
    four = fourth - fourth_remainder
    x = x - fourth

    fifth = x / 1
    fifth_remainder = x % 1
    five = fifth - fifth_remainder
    x = x - fifth

    print(one, two, three, four, five)