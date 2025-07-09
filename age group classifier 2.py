age=int(input(" enter a age "))
if age>=0 and age<=12:
    print( " child ")
elif age>=13 and age<=19:
    print(" teen")
elif age>=20 and age<=59:
    print(" adult")
else:
    print(" senior ")