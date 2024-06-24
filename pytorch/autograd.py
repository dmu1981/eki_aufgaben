import torch
from matplotlib import pyplot as plt

# Einleitung
############

# Mit PyTorchs AutoGrad System ist es möglich die Gradienten
# von mathematischen Operationen direkt berechnen zu lassen
# Dazu erzeugt man zunächst einen Tensor und teil Torch
# mit, dass man für diesen auch Gradienten benötigt. 
#w = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)

# Alle mit diesem Tensor durchgeführten Berechnungen ermitteln dann
# auch direkt den Gradienten
#x = torch.tensor([2])
#y = w[0]+w[1]*x+w[2]*(x**2)+w[3]*(x**3)
#print(y)

# Um die Gradietenberechnung zu starten muß zunächst von der Zielvariable
# ausgehend die backward() Methode ausgeführt werden
#y.backward()

# Der Gradient steht dann in w.grad
#print(w.grad)

# Aufgabe 1
###########
# Erzeugen Sie wie oben einen Gewichtstensor mit 3 Einträgen (w0, w1, w2).
# Hinweis: Sie können torch.rand()
# Berechnen Sie dann für das Modell
#
#   y = w0 + w1 * sin(x) + w2 * cos(x)
#
# das quadratische Residuum bezüglich des Punktes (x,y) = (0.5, 2.4), also
#
#   r = (y - 2.4)**2
#
# Bestimmen Sie dann mit r.backward() den Gradienten nach w und geben Sie diesen aus
# Hinweis: Verwenden Sie torch.sin und torch.cos, die eingebauten Funktionen von PyTorch
# Sie können auch torch.pow verwenden um 
w = torch.rand(3, requires_grad=True)
x = torch.tensor(0.5)
y = w[0] + w[1] * torch.sin(x) + w[2] * torch.cos(x)
r = (y - 2.4)**2
print(r)
r.backward()
print(w.grad)

# Aufgabe 2
###########
# Berechnen Sie nun den "Mean Square Error" bezüglich der unten gegebenen Daten
# Hinweis: Verwenden Sie torch.mean um den Mittelwert zu berechnen
x     = torch.tensor([-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0,  1.5, 2.0, 2.5])
ySoll = torch.tensor([ 1.5, -1.0 , 2.0,  1.0, -2.0, 0.0, 1.0, 0.5, -2.0, 0.0, 1.0])
yPred = w[0] + w[1] * torch.sin(x) + w[2] * torch.cos(x)
r = torch.mean((yPred - ySoll) ** 2)
print(r)
r.backward()
print(w.grad)

# Aufgabe 3
###########
# Erweitern Sie das Modell und berechnen Sie die Residuuen erneut
#
#  y = w0 + w1 * sin(w2 * x + w3) + w4 * cos(w5 * x + w6)
w     = torch.rand(7, requires_grad=True)
x     = torch.tensor([-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0,  1.5, 2.0, 2.5])
ySoll = torch.tensor([ 0.8,  1.2 , 1.7,  1.6,  1.2, 0.8, 0.6, 0.8,  1.2, 1.3, 1.0])
yPred = w[0] + w[1] * torch.sin(w[2] * x + w[3]) + w[4] * torch.cos(w[5] * x + w[6])
r = torch.mean((yPred - ySoll) ** 2)
print(r)
r.backward()
print(w.grad)

# Aufgabe 4
###########
# Implementieren Sie nun ein Gradientenabstiegsverfahren
# Führen Sie dazu 1000 Schritte aus mit einer Lernrate von 0.001
# Hinweis: 
#   Um die neuen Gewichte zu berechnen müssen Sie w.data überschreiben und w.grad auf None setzen.
#   
#       w.data = w.data - eta * w.grad.data
#       w.grad = None
#  
w     = torch.rand(7, requires_grad=True)
x     = torch.tensor([-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0,  1.5, 2.0, 2.5])
ySoll = 0.3 * x + 1.3*torch.sin(1.7*x - 0.9) #torch.tensor([ 0.8,  1.2 , 1.7,  1.6,  1.2, 0.8, 0.6, 0.8,  1.2, 1.3, 1.0])
eta   = 0.01
for i in range(5000):
    yPred = w[0] + w[1] * torch.sin(w[2] * x + w[3])# + w[4] * torch.cos(w[5] * x + w[6])
    r = torch.mean((yPred - ySoll) ** 2)
    print(r)
    r.backward()
    w.data = w.data - eta * w.grad.data
    w.grad.data.zero_()


xs = torch.linspace(-3.0, 3.0, 50)
y = w[0] + w[1] * torch.sin(w[2] * xs + w[3])
plt.plot(x,ySoll, 'r*')
plt.plot(xs,y.detach(),'k')
plt.show()