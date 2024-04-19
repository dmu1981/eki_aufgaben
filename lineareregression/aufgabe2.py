import numpy as np
from matplotlib import pyplot as plt

# Einleitung
############
# Wir haben wieder eine Meßreihe, diesmal mit 100 Datenpunkten.
noise = 0.1
coords_x = np.linspace(0,6.28,100)
coords_y = 1.0 + 2.0 * np.sin(coords_x) + 3.0 * np.cos(coords_x)
coords_x = coords_x + np.random.normal(0.0, noise, coords_x.shape)
coords_y = coords_y + np.random.normal(0.0, noise, coords_y.shape)

# Aufgabe 2a
############
# Plotten Sie die Koordinaten in ein Koordinatensystem um sich einen 
# Überblick zu verschaffen

# Aufgabe 2b
############
# Schätzen Sie nun wie in Aufgabe 1 ein lineares Modell der Form
#
#   y = w0 + w1 * sin(x) + w2 * cos(x)
#
# Geben Sie die geschätzten Modellparameter auf der Konsole aus


# Aufgabe 2c
############
# Plotten Sie die durch ihre Modellparameter geschätzte Funktion in das gleiche Koordinatensystem

