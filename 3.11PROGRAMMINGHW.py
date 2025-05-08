
totmi = 0
totgal = 0

for i in range(1000):
    gal = float(input("Enter the gallons used(-1 to end):"))

    if gal != -1:
        mi = float(input("Enter the miles driven: "))
        mpg = mi/gal
        print("The miles/gallon for this tank was", mpg)
        
        totmi = mi + totmi
        totgal = gal + totgal

    
    else:
        total = totmi/totgal
        print("The overall average miles/gallons was ", total)
        break

