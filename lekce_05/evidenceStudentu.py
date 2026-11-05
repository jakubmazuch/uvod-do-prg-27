body = {
    "Anna": [8, 9, 10],
    "Boris": [6, 7, 9],
    "Cyril": [10, 10, 8]
}

print("Původní body Anny:", body["Anna"])

body["Anna"][0] = 10

body["Damian"] = [10, 10, 10]

body["Cyril"].append(9)

prumer = sum(body["Boris"]) / len(body["Boris"])

print("Aktuální body Borise:", body["Boris"])
print("Součet bodů Borise:", sum(body["Boris"]))
print("Borisův průměr:", prumer)
