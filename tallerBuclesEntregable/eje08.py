import numpy as np
import os
nf = 4
nc = 5
sf = 0
sc = np.zeros(nc+1)
t = 0
a = np.zeros((nf,nc))
for i in range(0,len(a),1):
    for j in range (0,len(a[i]),1):
        os.system("cls")
        a[i][j] = input("ingrese un numero: ")

for i in range(0,len(a),1):
    sf = 0
    for j in range (0,len(a[i]),1):
        sf+= a[i][j]
        sc[j]+=a[i][j]
        print(f"{a[i][j]:4} ",end=" ")
    print(f"={sf:3}")

for i in range(0,len(sc)):
    if i==len(sc)-1:sc[i] = t
    t+=sc[i]
    print(f"={sc[i]:4}",end=" ")