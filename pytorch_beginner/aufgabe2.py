import torch
from tqdm import tqdm
from matplotlib import pyplot as plt


# Einleitung
# ##########
# Wir wollen zu diesen Daten wieder ein logistisches Regressionsmodell der Form
#
#   y = sigmoid(w0 + w1 * x + w2 * x**2 + w3 * x**3)
#
# mit Gradientenaufstiegsverfahren schätzen (vgl. früheres Praktikum). 
# Dazu betrachten wir diese Daten 
X = torch.tensor([[1.0, 2.0, 3.0, 4.0]])
y = torch.tensor([[1.0, 1.0, 0.0, 0.0]])

# # Wir beginnen mit Gewichten nahe 0
w = torch.tensor([0.01, 0.01, 0.01, 0.01], requires_grad=True)

bar = tqdm(range(5000))
for step in bar:
  # Wir erzeugen wieder die Prädiktion (Vorhergesagte Wahrscheinlichkeit)
  prediction = torch.sigmoid(w[0] + w[1] * X + w[2] * X**2 + w[3] * X**3)
  
  # Wir berechnen die zu maximierende Zielgröße (Likelihood)
  likelihood = torch.prod(torch.pow(prediction, y) * torch.pow(1.0 - prediction, 1.0 - y))

  bar.set_description(f"likelihood={likelihood.item():2f}")

  likelihood.backward()

  w.data = w.data + 0.005 * w.grad 
  w.grad.data.zero_()

print(f"{prediction[0][0].item()*100:.2f}%")
print(f"{prediction[0][1].item()*100:.2f}%")
print(f"{prediction[0][2].item()*100:.2f}%")
print(f"{prediction[0][3].item()*100:.2f}%")

# Aufgabe 1:
###########
# Kopieren Sie das Skript oben und passen Sie es an um
# das gegebene Regressionsproblem (Gradientabstieg!)
# mit LogCosh Loss zu lösen.
#
# Das Modell ist 
#
#   w[0] + w[1] * X + w[2] * X**2 + w[3] * X**3
#
# Berechnen Sie dann das Residuum und den summarischen LogCosh Loss.
#
# Hinweis: Reduzieren Sie die Lernrate (z.B. auf 0.00002)

# Wir beginnen mit Gewichten nahe 0



# Aufgabe 2:
###########
# Plotten Sie die Punkte sowie das Modell mit matplotlib
#
# Hinweis: Sie müssen mit w.detach() zunächst die Gradientenberechnung
# ausschalten 
w = w.detach()


