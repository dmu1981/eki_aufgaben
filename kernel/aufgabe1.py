import numpy as np
import math
from matplotlib import pyplot as plt

# Einleitung
# ##########
# In dieser Aufgabe haben wir die folgenden Punkte gegeben.
# Der Code visualisiert die Daten um Ihnen einen Überblick zu geben. 
#
# Die Daten sind offensichtlich nicht linear trennbar. Wir wollen daher
# eine lineare Regression mit RBF-Kernel durchführen.
X = np.array([[0,0],[0,1],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1],[-1,0]])
y = np.array([-1,-1,-1,-1,1,1,1,1])
plt.plot(X[4:, 0], X[4:, 1], "ok", ms=10)
plt.plot(X[4:, 0], X[4:, 1], "or", ms=8)
plt.plot(X[:4, 0], X[:4, 1], "ok", ms=10)
plt.plot(X[:4, 0], X[:4, 1], "ob", ms=8)
plt.show()

# Aufgabe 1
# #########
# Wir müssen zunächst die Kernel-Matrix K berechnen. Da wir insgesamt 8 Punkte
# gegbeen haben wird K eine 8x8 Matrix sein. Dabei entspricht der Eintrag 
# an der Stelle (i,j) dem Wert des Kernels 
#
#   k(xi, xj) = exp(-(||xi - xj||²))
#
# Hier sind xi bzw. xj die Koordinaten des i-ten bzw. j-ten Punktes aus X. 
#
# Hinweis: Es kann helfen die K-Matrix zunächst mit nullen in der gewünschten Größe
# zu initialisieren und dann mit zwei ineinander geschachtelten Schleifen zu befüllen
K = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        # TODO: Add your code here
        pass

# Aufgabe 2
# #########
# Um nun die Modellparameter im Kernel-Space zu bestimmen müssen wir K invertieren 
# und mit dem Klassenvektor y multiplizieren. Bestimmen Sie die Modellparameter und geben
# sie diese auf der Konsole aus.
        



# Aufgabe 3
# #########
# Wir wollen nun den neuen gegebenen Punkt Q (siehe unten) mit Hilfe unseres Modells klassifzieren.
# Dazu müssen wir wieder zunächst den Kernel für jede Kombination aus Punkten von X mit Q berechnen, also
# den 8-dimensionalen Vektor v mit
#
#   vi = k(xi, Q)
#
# Berechnen Sie v und geben sie v auf der Konsole aus
# Danach müssen wir das Skalarprodukt zwischen den Modellparametern (vgl. Aufgaben oben) und v berechnen.
# Geben sie auch dieses Skalarprodukt auf der Konsole aus und interpretieren Sie das Ergebniss
Q = np.array([0.75, -0.35])




# Aufgabe 4 (Bonus)
# #################
# Der folgende Code initialisiert mit np.linspace und np.meshgrid zwei
# 20x20 Matrizen xx und yy mit Werten zwischen je -1.5 und 1.5
# Ausserdem wird mit np.zeros_like eine 20x20 Matrix mit Namen z initialisiert, 
# die zunächst nur Nullen enthält.
#
# Berechnen Sie für jeden der 20x20 Punkte das jeweilige Klassifikationsergebniss,
# also das Skalarprodukt zwischen Modellparametern (vgl. Aufgabe 2) und dem 
# jeweiligen Vektor v (vgl. Aufgabe 3). Beachten Sie das v natürlich an jedem Punkt anders 
# ist und daher immer wieder neu berechnet werden muß.
#
# Verwenden Sie dann plt.contourf und plt.contour um die Klassifikationsentscheidungen
# sowie die Entscheidungsgrenze (also z = 0) zu zeichnen.
x_range = np.linspace(-1.5, 1.5, 20)
y_range = np.linspace(-1.5, 1.5, 20)
xx, yy = np.meshgrid(x_range, y_range)
z = np.zeros_like(xx)
for xidx, x in enumerate(x_range):
    for yidx, y in enumerate(y_range):
        # TODO: Add code to calculate z[yidx, xidx] here
