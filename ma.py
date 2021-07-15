import numpy as np
import matplotlib.pyplot as plt

                # Taille du cercle
depart=0          # Point de départ
n=1000               # Longueur d'une marche
K=15                # Nombre de marches

#plt.plot([0,n],[L,L],label='$L=$'+str(L)+'') # Barre horizontale a hauteur L

for k in range(K):
    TiragesAleatoires=2*(np.random.rand(n)<0.5)-1              # Tire n Bernoulli +1/-1
    SommeCumulee=(depart + np.cumsum(TiragesAleatoires))
    plt.plot(SommeCumulee)                                     # On ajoute la trajectoire à la figure
    plt.pause(0.05)

plt.title("Simulation de $K=$"+str(K)+" marches aleatoires")
plt.legend()
plt.show()
