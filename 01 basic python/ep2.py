print(" *** Wind classification ***\nEnter wind speed (km/h) : ",end="")
s = float(input());
print("Wind classification is ",end="")
if(s>=0):
    if(s<=51.99):
        print("Breeze.")
    elif(s<=55.99):
        print("Depression.")
    elif(s<=101.99):
        print("Tropical Storm.")
    elif(s<=208.99):
        print("Typhoon.")
    else:
        print("Super Typhoon.")