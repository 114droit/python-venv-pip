import matplotlib.pyplot as plt
import pandas as pd

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

# Datenanalyse mit pandas
data = {
    'Dezimalziffern': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Quadrate': [0**2, 1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2],
    'Kubisch': [0**3, 1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3]
}

df = pd.DataFrame(data).to_csv('zahlen.csv')
