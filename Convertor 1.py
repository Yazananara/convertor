#cel=(fahr-32)*1.8;
fah=float(input("enter degree in farenhiet: "))
cel=(fah-32)*1.8;
print("%0.1f degrees farenhiet is equal to %0.1f degrees celcius"%(fah,cel));
temp=cel
if temp>=60:
    print("Its too hot")
elif temp<=20:
    print("its too cold")
else:
    print("its nice...")