import torch 

# Einleitung
# ##########
#
# In dieser ersten Aufgaben wollen wir das AutoGrad System von PyTorch kennenlernen
# Dieses System berechnet für durchgeführte Operationen automatisch im Hintergrund
# den Gradienten und bildet somit die Grundlage für modernes maschinelles Lernen
#
# Wir wollen ganz konkret das Polynom
#
#   y = w0 + w1 * x + w2 * x² + x3 * x³
#
# mit vier Parametern w0, w1, w2 und w3. 
#
# Damit PyTorch für diese Parameter die Gradienten mit berechnet erzeugen wir einen Tensor 
# und aktivieren die Gradientenberechnung
x = 2.0
w = torch.tensor([1.0, 1.0, 1.0, -1.0], requires_grad=True)

# Wir berechnen nun den y-Wert wie in der Einleitung angegeben und geben diesen auf der Konsole aus
# Da w ein Tensor ist wird auch ihr Ergebnisswert y ein Tensor sein. Rufen Sie dessen backward() Methode auf
# um die Gradientenberechnung zu starten. Geben Sie dann w.grad auf der Konsole aus und interpretieren Sie 
# das Ergebnis. Rufen Sie anschließend w.grad.zero_() auf um die Gradienten wieder auf 0 zu setzen.
print("Linear Modell")
y = w[0] + w[1] * x + w[2] * x**2 + w[3] * x**3
print(y)
y.backward()
print(w.grad)
w.grad.zero_()

# Aufgabe 1
# #########
# Verändern Sie das Modell indem Sie die folgenden Varianten ausprobieren. Geben Sie jeweils
# den Gradienten aus und interpretieren Sie das Ergebniss. Leiten Sie den Gradienten selbst her und vergleichen Sie
#
#   (1) y = torch.cos(w[0] * x) 
#           für x=pi/2
#
#   (2) y = torch.log(torch.cosh(w[0] + w[1] * x))
#           für x=0.5
#           
#   (3) y = torch.sigmoid(w[0] * x)
#           für x=1.0
#