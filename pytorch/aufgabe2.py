import torch
from torch import nn
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

# Einleitung
# ##########
#
# Wir tauschen nun den Datensatz gegen CIFAR10 aus
#
#   https://www.cs.toronto.edu/~kriz/cifar.html
#
# Der Datensatz besteht aus 60.000 Farbbildern (3 Eingangskanäle) und insgesamt 10 Klassen. 
dataset = torchvision.datasets.CIFAR10("cifar10", 
                                       download=True,
                                       train=True,
                                       transform=torchvision.transforms.ToTensor())

loader = DataLoader(dataset, batch_size=16, shuffle=True)

dataset_test = torchvision.datasets.CIFAR10("cifar10", 
                                       download=True,
                                       train=False,
                                       transform=torchvision.transforms.ToTensor())

loader_test = DataLoader(dataset_test, batch_size=16, shuffle=True)

batch, labels = loader.__iter__().__next__()
grid = torchvision.utils.make_grid(batch, 4).permute(1,2,0)
plt.imshow(grid)
plt.show()

# Aufgabe 1
# Passen Sie das FullNet aus Aufgabe1.py an den CIFAR10 Datensatz an. 
# Die Bilder aus CIFR10 sind 32x32 Pixel groß mit 3 Farbkanälen (Rot/Grün/Blau)
class FullNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()
        self.sigmoid = nn.Sigmoid()

        # TODO:
        # Erzeugen Sie hier mit Hilfe des nn.Linear Moduls
        # drei Schichten mit sinnvoller Eingabe- und Ausgabegröße
        # Hinweis: Die Bild-Daten haben eine Auflösung von 32x32 Pixeln mit 3 Kanälen
       
    def forward(self, x):
        # TODO: 
        # Implementieren Sie den Forward-Pass ihres Netzwerkes
        # indem Sie die Daten zunächst flatten und dann suksezive 
        # durch die linearen Schichten und den Sigmoid geben. 
        # ACHTUNG: Auf der letzten Schicht brauchen Sie keine Nicht-Linearität
       
        return x

# Aufgabe 2
# Passen Sie nun wieder das ConvNet aus Aufgabe2 an CIFAR10 an. 
#
# HINWEIS:
# Denken Sie daran das sie weiter unten im Code ihr ConvNet instantieren
# müssen anstatt dem FullNet von oben
class ConvNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.relu = nn.ReLU()
        self.flatten = nn.Flatten()
        
        # TODO: 
        # Erzeugen Sie mittels nn.MaxPool2D und nn.Conv2d 
        # geeigente Layer. Eine gute Architektur könnte z.B. aus insgesamt 3 Faltungslayern
        # mit anschließendem Pooling bestehen. Die ersten beiden Ebenen könnten mit 5x5 Masken
        # arbeiten während die dritte Faltungsebene mit einer 3x3 Maske auskommt. 
        # Überlegen Sie dann wieviele Neuronen ihr Netzwerk nach den Faltungen noch hat     
        # und fügen Sie geeignete Fully-Connected Layer am Ende hinzu. Eine gute Architektur
        # könnte hier z.B. eine verstecke Schicht verwenden, also z.B. so:
        #
        #  Input -> Conv(5,5) -> Pool -> ReLU  
        #        -> Conv(5,5) -> Pool -> ReLU 
        #        -> Conv(3,3) -> Pool -> ReLU
        #        -> Flatten
        #        -> Linear -> ReLU
        #        -> Linear

        
    def forward(self, x):
        # TODO:
        # Implementieren Sie den Forward-Pass ihres Faltungsnetzwerkes
        # indem Sie immer abwechseln zwischen Faltung und Pooling + ReLU. 
       
        # Flatten Sie dann das Ergebniss und wenden Sie den letzten Fully-Connected Teil
        # an um ihr Ergebniss zu erzeugen
        
        return x

net = ConvNet() ## ACHTUNG: Hier müssen sie für Aufgabe 2 das ConvNet instantieren anstatt das FullNet
optim = torch.optim.Adam(net.parameters(), lr=0.001)
criterion = torch.nn.CrossEntropyLoss()


### AB HIER BRAUCHEN SIE NICHTS ZU TUN AUSSER ZU VERSTEHEN WAS PASSIERT
for epoch in range(10):
    total_loss = 0
    total_cnt = 0
    total_correct = 0

    bar = tqdm(loader)
    for batch, labels in bar:
        optim.zero_grad()

        out = net(batch)
        loss = criterion(out, labels)
        loss.backward()
        
        total_correct += torch.sum(torch.argmax(out, dim=1) == labels)
        total_loss += loss.item()
        total_cnt += batch.shape[0]

        bar.set_description(f"train: epoch={epoch}, loss={1000.0*total_loss / total_cnt:.3f}, acc={total_correct / total_cnt * 100:.2f}%")

        optim.step()

    total_loss = 0
    total_cnt = 0
    total_correct = 0

    bar = tqdm(loader_test)
    for batch, labels in bar:
        with torch.no_grad():
            out = net(batch)
            loss = criterion(out, labels)
        
        total_correct += torch.sum(torch.argmax(out, dim=1) == labels)
        total_loss += loss.item()
        total_cnt += batch.shape[0]

        bar.set_description(f"test: epoch={epoch}, loss={1000.0*total_loss / total_cnt:.3f}, acc={total_correct / total_cnt * 100:.2f}%")
