print("Bitte geben Sie die gefragten Angaben ein")

print("Marke eingeben, bitte erster Buchstabe klein und ohne Bindestriche:")

x1 = int(input())

print("Kilometerstand eingeben, bitte nur ganze Zahlen eingeben:")

x2 = int(input())

print("PS eingeben, bitte nur Zahlenverwenden:")

x3 = int(input())

print("Leergewicht eingeben, bitte nur ganze Zahlen eingeben:")

x4 = int(input())

print("Getriebsart eingeben, Auswahl = Schaltgetriebe, Automat oder Automat Sequentiell, - :")

x5 = int(input())

print("Hubraum eingeben, bitte nur Zahlen verwenden:")

x6 = int(input())

print("Antribesart eingeben, Auswahl = Allrad, Vorderradantireb, Hinterradantrieb, - ")

x7 = int(input())

print("Anzahl Türen:")

x8 = int(input())

print("Anzahl Sitze:")

x9 = int(input())

print("Treibstoffart eingeben, Auswahl = Benzin Bleifrei, Benzin verbleit,Diesel,Elektrisch,Hybrid :")

x10 = int(input())

print("Verbrauch pro 100km eingeben, bitte nur Zahlen verwenden:")

x11 = int(input())




t1 = 0
t2 = 0.60728501
t3 = -0.04215118
t4 = -0.08041125
t5 = 0.04965925
t6 = -0.01676428
t7 = -0.00089649
t8 = 0.05744553
t9 = -0.06702858
t10 = 0.03630458
t11 = -0.00667139

y = x1*t1 + x2*t2 + x3*t3 + x4*t4 + x5*t5 + x6*t6 + x7*t7 + x8*t8 + x9*t9 + x10*t10 + x11*t11

print("Ihr Auto hat den Wert von " + str(y) + " CHF")
