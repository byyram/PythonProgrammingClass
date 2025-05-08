
print("Celsius\tFahrenheit") #getting a "title" in the terminal

for celsius in range(101): #will iterate through first 0-100
    fahr = celsius * (9/5) + 32 #calculating fahrenheit

    new_cel = "{:.1f}".format(celsius) #formatting for one decimal place
    new_fahr = "{:.1f}".format(fahr)

    print(new_cel,"\t", new_fahr)

