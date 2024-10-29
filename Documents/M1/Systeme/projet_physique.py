
Longueur_onde=[]
Intensité=[]
fd=open("Spectre_photoluminescence.txt")
for l in range (25):
    next(fd)

    
for ligne in fd:
    data=ligne.strip().split()
    print(data)
    Longueur_onde.append(data[0])
    Intensité.append(data[1])
print(Longueur_onde)
print(Intensité)
fd.close()
