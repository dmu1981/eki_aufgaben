import csv
from sklearn import feature_extraction
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np

# Einleitung
# ##########
# In dieser Aufgabe wollen wir einen einfachen Klassifikator für 
# SPAM-Mails entwickeln. Die Datei "spam.csv" enthält dabei einen
# Datensatz von Mails die bereits in SPAM und HAM (kein SPAM) sortiert wurden.
# Der folgende Code lädt diese Datei und sortiert die Nachrichten in 
# zwei Python-Listen (HAM und SPAM ein.)
ham    = []
spam   = []

with open("spam.csv", "rt") as f:
    reader = csv.reader(f)
    for label, text in reader:
        if label=="ham":
            ham.append(text)
        else:
            spam.append(text)

bodies = spam + ham
labels = np.concatenate([
            np.zeros(len(spam)),
            np.ones(len(ham))])
         
# Aufgabe 1
# #########
# Wir müssen die in Text-Form vorliegenden Mails zunächst 
# in eine besser geeignete Form für machine-learning überführen.
# Verwenden Sie den CountVectorzer des SKLEARN-Packages
# 
#   https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
#
# Um sowohl die SPAM-Mails als auch die HAM-Mails jeweils in eine solche
# zu überführen. Verwenden Sie dann die get_feature_names_out() Methode
# um die häufigsten Wörter sowohl für SPAM- als auch HAM-Mails auf der Konsole auszugeben.


# Aufgabe 2
# #########
# Kombinieren Sie nun beide Vokabulare zu einem neuen, welches
# beide Wörterlisten enthält. 
#
# Hinweis: Sie können die Rückgabewerte der get_feature_names_out() Methode
# mit list(...) in eine Python-Liste umwandeln. Sie können dann die Listem
# mit Hilfe des Plus-Operators aneinanderfügen, also 
#
#   merged = listeA + listeB
#
# Um doppelte Einträge zu entfernen können Sie diese Liste dann zunächst
# in ein Python-Set (Menge) umwandeln und diese dann wieder zurück in eine
# Liste umwandeln, also
#
#   liste = list(set(liste))
#
# Geben Sie diese Liste der kombinierten Wörter ebenfalls auf der Konsole aus.
# Wieviele sind es?


# Aufgabe 3
# #########
# Erzeugen einen neuen CountVectorizer mit dem von ihnen in 
# Aufgabe 2 erzeugten, kombinierten Vokabular. 
# Kombinieren Sie die Liste der eMails (spam und ham) genauso 
# wie die Liste der Wörter (vgl. oben) und wenden Sie die transform(...)
# Methode des CountVectorizers an um die Mails in eine entsprechende
# Vektor-Repräsentation zu überführen.
#
# Der Count-Vectorizer gibt eine s.g. Sparse-Matrix zurück.
# Mit Hilfe der toarray() Methode können Sie diese in ein normales Array überführen.
#
# Wandeln Sie die Labels-Liste (labels) ebenfalls in ein numpy-Array um indem
# sie schreiben
#
#   y = np.array(labels)
#
# Geben Sie die vektorielle Repräsentation einiger der Mails aus indem Sie
# schreiben
#
#   print(x[5])
#
# falls x die von transform(...) und toarray(...) erzeugte Matrix ist. 


# Aufgabe 4
# #########
# Verwenden Sie die train_test_split Methode von SkLearn
#
#   https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
#
# um ihre Daten in ein Trainings- und ein Testset zu teilen. Verwenden Sie
#
#   test_size = 0.33
#
# um 33% der Daten dem Testset hinzuzufügen. 


# Aufgabe 5
# #########
# Verwenden Sie die LinearSVC Klasse von SkLearn um ein 
# Support-Vektor-Machine zu erstellen. Verwenden Sie einen linearen Kernel.
#
#   https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC
#
# Verwenden Sie die fit(...) Methode um ein Modell an ihre Daten anzupassen.
#
# Verwenden Sie dann die predict(...) Methode um eine Vorhersage für die 
# Trainings- und Test-Daten zu erzeugen. 


# Aufgabe 6
# #########
# Nachdem Sie die Modellparameter mit Hilfe der fit(...) Methode bestimmt haben
# enthält die svc Klasse eine neue Variable Namens coef_ (vgl. offizielle Doku).
# Diese enthält die Modellparameter (also Gewichte) ihrer Support-Vektor-Maschine.
# Geben Sie die Einträge zusammen mit den ihnen entsprechenden Wörtern aus und
# interpretieren Sie das Ergebniss. Geben Sie auch die intercept_ Variable
# aus. Interpretieren Sie auch diese.


# Aufgabe 7
# #########
# Vergleichen Sie die Prädiktion mit dem GroundTruth um zu messen
# wieviele Beispiele sie korrekt vorhergesagt haben. Teilen Sie 
# jeweils durch die Zahl der gesamten Mail in beiden Sets um die
# Genauigkeit (Accuracy) auf ihren beiden Sets zu bestimmen.
# Geben sie beide Genauigkeiten auf der Konsole aus. 
