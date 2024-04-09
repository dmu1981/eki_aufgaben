import numpy as np
from matplotlib import pyplot as plt

# Einleitung
############
# Wir haben eine Meßreihe mit 4 Datenpunkten aufgenommen und gemessen
#
#      x | 1 | 2 | 3 | 4
#       -----------------
#      y | 3 | 4 | 4 | 2
#
# Wir möchten ein linears Modell der Form
#
#   y = w0 + w1*x + w2*x² + w3x³ 
#
# schätzen und dazu die vier Parameter w0, w1, w2 und w3 bestimmen.

# Aufgabe 1a
############
# Definieren Sie geeignte NumPy Arrays um die gegebenen Daten verwenden zu können.
# Verwenden Sie die Funktionen np.ones_like und np.stack um die aus der Vorlesung bekannte
# X-Matrix für das gegebenen Modell aufzustellen.



# Aufgabe 1b
############
# Bestimmen Sie nun mittel np.linalg.inv die Pseudeoinverse von X sowie die Modellparameter w0,w1,w2 und w3
# Geben Sie diese auf der Konsole aus. Berechnen Sie ebenfalls
# den summarischen quadratischen Fehler ihrer Vorhersage und geben Sie auch diese auf der Konsole aus.

# Aufgabe 1c
############
# Plotten Sie die Meßreihe sowie das geschätzte Modell 


# Aufgabe 1d
############
# Was verändert sich wenn Sie ihrer Meßreihe weitere Koordinaten hinzufügen, z.B den
# Punkt (5,2)?


