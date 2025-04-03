import numpy as np 
import  pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel(
    'C:/Users/hzhci/Desktop/speech_mode_2.xlsx') #importiert die Daten in den Python-Interpreter

# print(df) Kontrollanweisungen, um zu prüfen ob den DataFrame richtig und vollständig importiert wurde

y = df['monosyllabic_score'] #Siehe DocStrings



predictors = [
    'hearingaid_years_ipsi',
    'hardhearing_years_ipsi',
    'deaf_years_ipsi',
    'Insertion_Angle_(IA)',
    'mean_low_preop_AC',
    'PBmax',
    'age_atimplantation_years',
    'mean_IFT'] #Siehe Docstrings

"""
Ein Pandas Series Object wurde erstellt für alle Werte aus der Datei Speech_mode_2 für monosyllabic_score.
Der Score entspricht der Zielvariable und wird gegen die Variablen 'hearingaid_years_ipsi','hardhearing_years_ipsi',
'deaf_years_ipsi', 'Insertion_Angle_(IA)','mean_low_preop_AC','PBmax',
'age_atimplantation_years', 'mean_IFT' geplottet
"""


fig, axes = plt.subplots(2, 4, figsize=(25,10))     
axes = axes.flatten()

"""         
subplots ist eine Funktion des Moduls Pyplots von Matplotlib und erstellt 2x4, also 8 leere Figures/Axes mit den # angegebenen Größen 25 und 10 in Zoll.
axes.flatten ist ein Attribut von der Bibliothek numpy und wandelt multidimensionale Arrays in eindimensionale Arrays, damut über mehrere Achsen itiert werden kann ohne eingenistete For-Schleifen einsetzen zu müssen.
"""


for i, predictor in enumerate(predictors):          
    x = df[predictor]
    """
    for-Schleife für jedes Element in der Liste predictors, die dann als Schlüssel für df verwendet wird in der nächsten Zeile
    entspricht jeden Wert in Predictor, wird dann in x_clean als bereinigte Daten gespeichert
    eine For-Scheife die über die Werte der Liste Predictors itiert, damit eine Grafik für jeden Predictor mit dem
    folg. Code erstellen lässt.
    """

    mask = ~x.isna() & ~y.isna()
    x_clean = x[mask]
    y_clean = y[mask]

    """
    Daten auf der x und y-achsen werden bereinigt, Null Werte ignoriert
    indem eine Maske erstellt wird x.isna() gibt den Wert True zurück wenn der Wert Null ist, ~x.isna gibt True zurück wenn der Wert not Null ist.
    Diese Werte werden dann als Filter benutzt, um die gefilterte Werte zurückzugeben.

    """

    n = len(x_clean) #length of x_clean wurde für d

    r,p = stats.pearsonr(x_clean, y_clean) #durchführung von Person's R, Tuple Unpacking in r und p.

    slope, intercept, r_value, p_value, std_error = stats.linregress(x_clean, y_clean)
    #linear regression für x_clean and y_clean, nochmal tuple unpacking in die obigen Variablen

    line = slope * x_clean + intercept # y = mx +  c 

    R_squared = round(r_value**2,4) #Wert für R_Squared, abgerundet zu der 4. Dezimalstelle
    
    ax = axes[i] # damit über jedes eindimensionale Arrays itiert wird.

    scatter = ax.scatter(x_clean, y_clean, s = 20, color = "blue", alpha = 0.7)
    #Erstellung des Scatterplots -hierzu noch mehr Modifikationen für die Anzahl/Häufigkeitsberechnung

    x_sorted = np.sort(x_clean) # Die Werte von x_clean werden in aufsteigender Reihenfolge sortiert was für die Abbildung der Regressionslinie verwendet wird
    y_fit = slope * x_sorted + intercept

    ax.plot(x_sorted, y_fit, color = "blue", linestyle='solid') #Best-Fit Linie geplottet mit axes[i].plot
    
    """ab diesem Punkt wurde künstliche Intelligenz in Anspruch genommen um die Betitelung für die Grafiken zu erstellen"""

    ax.text(1.09, 0.75, f'n = {n}\nr ={r:.2f}\nR² = {R_squared:.2f}\np = {p:.3f})',
    transform = ax.transAxes, fontsize=12, verticalalignment='baseline',
    bbox=dict(boxstyle='square',facecolor = 'white',alpha = 1))

    ax.set_xlabel(predictor)
    ax.set_ylabel('monosyllabic_score')
    ax.set_title(f'{predictor} vs. monosyllabic score')

if len(predictors) < len(axes):
    for j in range(len(predictors), len(axes)):
        fig.delaxes(axes[j])

"Dieser Block sorgt dafür, dass unbenutze Subplots gelöscht werden"
        
        
plt.suptitle('Matplotlib Version - Monosyllabic Score - speech_mode_20250318', fontsize = 40) # Titel der Grafikeb
plt.tight_layout() #automatische Anpassung der multiplen Subplots
plt.show()