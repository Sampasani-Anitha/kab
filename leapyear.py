year=int(input("enter the values:"))

leap=False

if year%100 == 0 and year%400!=1:
    leap=False
elif year%4==0:
    leap=True
else:
    leap=False
print(leap)


