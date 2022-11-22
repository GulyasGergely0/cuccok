import sqlite3

data = []
adat = []
with open("elements.txt", encoding="UTF-8") as file:
    for sor in file:
        sor.strip().split("\t")
        data.append(sor)
print(data)
