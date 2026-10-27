a = abs(int(input("Zadejte celé číslo: ")))

if a < 10:
    print("Číslo je jednociferné.")
elif a < 100:
    print("Číslo je dvouciferné.")
elif a < 1000:
    print("Číslo je trojciferné.")
elif a < 10000:
    print("Číslo je čtyřciferné.")
elif a < 100000:
    print("Číslo je pěticiferné.")
else:
    print("Číslo má mnoho cifer.")
