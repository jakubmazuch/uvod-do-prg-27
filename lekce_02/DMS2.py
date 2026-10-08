uhel = float(input("Zadejte úhel v desitinných stupních: "))

D = int(uhel)
M = int((uhel - D) * 60)
S = (((uhel - D) * 60) - M) * 60


print(D, "°", M, "'", round(S, 3), "''")
