import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

# SciKit Learn kommt mit einigen fertigen Datensets 
# zum experimentieren. Eines davon ist das "DIGITS"-Datenset
# (https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html)
# welches mit der load_digits() Methode geladen werden kann.
dataset = load_digits()

# Das Datenset besteht aus 1797 Beispielen von handgeschriebenen Ziffern
# von 0 bis 9. Diese sind jeweils als 64-dimensionale Vektoren hinterlegt, die
# aber eigentlich Bilder mit 8x8 Pixeln (64 Pixel insgesamt) sind.
# Das dictionary enthält mit dem Key "target" die korrekte Zielklasse während der Key "data"
# die vektoriellen Bilddaten enthält. So kann man z.B. mit dem folgenden Code alle 
# Bild-Vektoren der Ziffer 4 finden
index_4 = dataset["target"] == 4
all_fours = dataset["data"][index_4]

# Um sich einen Eindruck von den Daten zu verschaffen kann man mehre dieser Vektoren
# also 8x8 Bild uminterpretieren und mit matplotlib anzeigen
fig, axs = plt.subplots(4,5)
for row in range(4):
    for col in range(5):
        img = all_fours[row*5+col].reshape(8,8)
        axs[row][col].imshow(img)

plt.show()

# Aufgabe 1
# #########
# Verwenden sie wieder die train_test_split(...) Methode von sklearn
# um die Data in ein unabhängiges Trainings- und Testset zu teilen.
#
# Trainieren Sie dann wie in der vorherigen Übung eine lineare Support-Vektor Maschine
# um die Ziffern zu klassifzieren. Beachten Sie das die sklearn Implementierung 
# der LinearSVC bereits mit nicht-binären Problemen umgehen kann. SKLEARN trainiert
# in dem Fall einfach "one-vs-rest", d.h. für jede Ziffer wird eine SVM trainiert
# wobei die jeweils anderen Ziffern in der Negativ-Klasse sind.
#
# Verwenden Sie die SVC.fit(...) Methode um die SVM zu trainieren
# und SVC.predict(...) um Prädiktionen für beide Sets zu erstellen. 
#
#   https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html



# Aufgabe 2
# #########
# Implementieren Sie die evaluate(...) Methode um aus den Vorhersagen sowie den tatsächlichen Klassen
# für jede Ziffer precision, recall sowie F1-Score zu bestimmen. 
def evalulate(predictions, targets, clsIndex):
    pass



# Aufgabe 3
# #########
# Geben Sie nun für jede Ziffer Precision, Recall und F1-Score sowohl auf dem Trainings- als auch
# dem Testset aus. Bestimmen Sie ebenfalls der Balanced Accuracy.
#
# Hinweis: Bei einem Multi-Klassen Problem ist die Balanced Accuracy identisch zum durchschnittlichen
# Recall.