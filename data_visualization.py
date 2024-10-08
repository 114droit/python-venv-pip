import matplotlib.pyplot as plt

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen
z = [i**3 for i in x]  # Kubikzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')
plt.plot(x, z, label='Kubikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadrat-/Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('3.Potenz')

# Legende anzeigen
plt.legend()

# Diagramm speichern
plt.savefig("quadratkubikplot.png")

# Diagramm anzeigen
plt.show()
