import numpy as np

## Aufgabe 2a
#############
#
# Wir wollen im folgenden die Funktion
#
#   f(x,y,z) = (x-3)^2 + (y-2)^2 + (z+5)^2
#
# betrachten. Bestimmen Sie den Gradieten der Funktion und implementieren Sie zwei
# Funktionen f und grad_f. Die Funktion f soll zu einem Tripel (x,y,z) den dazugehörigen
# Funktionswert an der gegebenen Stelle liefern. Die Funktion grad_f soll zu einem Tripel (x,y,z)
# den Gradienten liefern. 
#
# Hinweis: Sie können ihre Funktionen mit bekannten Werten testen, so ist z.B.
#
#   f(3,2,-5) = grad_f(3,2,-5) = (0,0,0)
#   
# und
#
#   f(0,0,0) = 38 während grad_f(0,0,0) = (-6,-4,10)
#
# ist.




## Aufgabe 2b:
##############
#
# Implementieren Sie nun ausgehend vom Startpunkt x_0 = (12, -5, 9)
# ein Gradientenabstiegsverfahren mit einer Lernrate von eta=0.05
# Berechen Sie dazu iterativ 100 mal sowohl der Funktionswert als auch
# den Gradienten am aktuellen Punkt. Setzen Sie dann
#
#   x_(n+1) = x_n - eta * grad_f(x_n)) 
#
# Geben Sie in jedem Schritt sowohl die Koordinate x_n aus sowie den 
# Gradienten an der Stelle.
