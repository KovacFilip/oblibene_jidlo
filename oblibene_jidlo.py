print("this code is now available on github")

jidlo = input("Zadej svoje oblibene jidlo: ")
if not jidlo:
    exit()

with open("oblibene_veci.txt", "w") as f:
    f.write(jidlo)
