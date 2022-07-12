C=float(input("Enter degrees in celcius: "))
fah=(C*1.8)+32
print("%0.1f degrees celcius is equal to %0.1f degrees farenhiet"%(C,fah));
Temp=fah
if Temp>=104:
    print("its too hot")
elif Temp<=50:
    print("its too cold")
else:
    print("its nice")