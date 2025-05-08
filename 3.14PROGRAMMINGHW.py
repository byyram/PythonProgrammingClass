pi = 0

for i in range(20000):
    x = -4
    adder = (x * ((-1)**(i+1)))/(2*i+1)
    
    pi = adder + pi
    print("The terms on the infinite series is:", i, "and the approximation is:", pi)

