import numpy as np
from matplotlib import pyplot as plt
import pickle

# Einleitung
############
#
# Sie sind Teil eines internationalen Teams aus Physikern und Datenwissenschaftlern.
# Als ersten Test einer guten Zusammenarbeit soll ihr Team die Gravitationskonstante der Erde 
# bestimmen. Ihre Physikkollegen schlagen dazu einen Frei-Fall-Test vor, d.h. ein Gegenstand 
# wird auf bekannter Höhe (100m) in einer Vakuumröhre fallen gelassen. Die Höhe des Gegenstands
# im freien Fall wird zu verschiedenen Zeitpunkten mittels Radar gemessen und in einer Zeitreihe 
# aufgetragen. Ihr Physikerkollegen haben ihnen die aktuellste Datenmeßreihe geschickt und 
# sie gebeten daraus eine möglichst gute Schätzung abzuleiten. 
#
# Das folgende Skript öffnet die Daten und speicher sie in zwei numpy-Arrays (time und height)
with open("data.pk", "rb") as f:
  time,height = pickle.loads(f.read())

# Aufgabe 1
# #########
# Visualisieren Sie die Daten mittels MatPlotLib um sich einen ersten Überblick zu verschaffen




# Aufgabe 2
# #########
# Offensichtlich sind die Daten mit Ausreißern kontaminiert. Versuchen Sie dennoch zunächst eine
# Schätzung mit Hilfe eines linearen Regressionsmodells. 
# Hinweis: Ihr Modell lautet 
#   
#     h = 100m - a * t²
#
# und hat somit nur einen Parameter (a). Überlegen Sie wie Sie die bekannte Ausgangshöhe (100m)
# einbauen können 
  



# Aufgabe 3
# #########
# Implementieren Sie nun 500 Schritte eines Gradientenabstiegsverfahren um ihre Schätzung zu verbessern.
# Verwenden Sie dazu den MAE-Loss wie in der Vorlesung diskutiert. Starten Sie mit der (absichtlich falschen) 
# Annahme a=0.0m/s² und einer Lernrate von 0.005. 
# Geben Sie in jedem Schritt die aktuelle Schätzung (a), den MAE sowie den Gradienten aus.
#
# Was fällt ihnen gegen Ende der 500 Schritte auf?
#
# Bonus: Zeichnen Sie in jedem 10.ten Schritt die Daten sowie die von ihrem Modell geschätzte Fall-Kurve. Verwenden
# Sie plt.pause(0.01) um die Darstellung zu ermöglichen ohne auf einen Tastendruck warten zu müssen.



# Aufgabe 4
# #########
# Implementieren Sie nun wieder 500 Schritte eines Gradientenabstiegsverfahren um ihre Schätzung zu verbessern.
# Verwenden Sie dazu aber der LogCosh-Loss wie in der Vorlesung diskutiert. Starten Sie wieder mit der 
# (absichtlich falschen) Annahme a=0.0m/s² und einer Lernrate von 0.005. 
# Geben Sie in jedem Schritt wieder die aktuelle Schätzung (a), den LogCosh-Loss sowie den Gradienten aus.
#
# Bonus: Zeichnen Sie in jedem 10.ten Schritt die Daten sowie die von ihrem Modell geschätzte Fall-Kurve. Verwenden
# Sie plt.pause(0.01) um die Darstellung zu ermöglichen ohne auf einen Tastendruck warten zu müssen.





# Aufgabe 5
# #########
# Berechnen Sie für a=9.81m/² und jeden Datenpunkt das Residuum r sowie den hyperbolischen Tangens von r.
# Berechnen Sie dann den Quotienten des hyperbolischen Tangens mit dem tatsächlichen Residuum.
# Plotten Sie die Daten farbig, wobei sie den Betrag des Quotienten für die Farbkodierung verwenden. Interpretieren
# sie das Ergebniss.
#
# Hinweis: Verwenden Sie plt.scatter mit der "coolwarm"-Colormap (cmap Parameter)
#
#   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html





  
    


