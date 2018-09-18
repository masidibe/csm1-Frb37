#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import methodes
import equations

# Résolution approchée de y' = 1-y avec y(0) = 5 pour t dans [0,1]
equations.a = -1.
equations.b = 1.
t0,y0 = 0.,5.
T = 1.
# Avec un pas de 0.2, il faut donc 5 iterations
h = [0.2, 0.1, 0.05, 0.025]
Err = []
for i in range(len(h)):
    N=int(T/h[i]) #recalcul du nombre d'itérations par pas
    [t,y1] = methodes.euler_explicite(t0,h[i],N,y0,equations.f_affine)
    # Solution exacte aux mêmes instants
    z1 = equations.sol_affine(t,y0)
    # Calcul de l'erreur maximum relative
    e1 = np.max(np.abs((z1-y1)/z1))
    Err.append(e1)
    # Affichage et sauvegarde du graphe des solutions exactes et approchées
    plt.plot(t,y1,'b-+',label='solution approchée h=0.1')
    plt.plot(t,z1,'r-',label='solution exacte')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("Méthode d'Euler explicite")
    plt.legend()
    plt.show()
    plt.savefig('euler_explicite_%2u.png'.format(i))

# Écriture de l'erreur en fonction de h et impression du graphique
print("{0} | {1}".format(h,Err))
plt.loglog(h,Err)
plt.xlabel('h')
plt.ylabel('Err')
plt.title('Err = f(h) (logarithmique)')
plt.legend()
plt.show()
plt.savefig('Err_fct_h.png')
