import numpy as np
from matplotlib import pyplot as plt

# Einleitung
# #########
# Ähnlich wie in Aufgabe 1 betrachten wir wieder ein Zwei-Klassen Problem aber mit unterschiedlichen
# Datenpunkten
# 
# Rot  (-1,-1), (-1,1), (1,-1), (1,1)
# Blau  (-0.25, 0.0), (0.25, 0.0), (-0.75, 0.0), (0.75, 0.0)

# Aufgabe 2a
# ##########
# Lösen Sie das lineare Regressiondsproblem wie in Aufgabe 1, d.h.
# zeichen Sie zuerst und bestimmen Sie dann die Modellparameter.
#
# Passen Sie dann das Modell an und verwenden Sie stattdessen
#
#   y = w0 + w1 * x1 + w2 * x2 + w3 * x2^2
# 
# als Model. Schätzen Sie auch hier die Trennfläche und zeichen Sie ebenfalls.


# Aufgabe 2b
# ##########
# Schätzen Sie nun wie in der vorherigen Aufgaben ein linears Modell der Form
#
#   y = w0 + w1 * x1 + w2 * x2 + w3 * x2^2
#
# indem Sie die X-Matrix aus der Vorlesung aufstellen, die Pseudoinverse bestimmen und
# dann die Modellparameter bestimmen. 


# Aufgabe 2c
# ##########
# Bringen Sie diesen Code ans Laufen indem Sie ggf. die Variablen w0, w1 und w1 an ihr Skript anpassen.
#
# x1, x2 = np.meshgrid(np.linspace(-2,2,10), np.linspace(-2,2,10))
# z = w0 + w1 * x1 + w2 * x2  + w3 * x2 * x2 
# plt.contourf(x1, x2, z, levels=[-10,0,10], colors=["b","r"], alpha=.2)
# plt.contour(x1, x2, z, levels=[0], colors=["k"])
# plt.xlim((-2,2))
# plt.ylim((-2,2))
# plt.show()