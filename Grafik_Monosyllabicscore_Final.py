import numpy as np
import  pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_excel('C:/Users/hzhci/Desktop/speech_mode_2.xlsx') 

#print(df.head()) Kontrollanweisungen, um zu prüfen ob den DataFrame richtig und vollständig importiert wurde

y = df['monosyllabic_score'] #Siehe Erklärung 1

df['age_atimplantation_years'] = df['age_atimplantation_years']/1_000_000
df['hearingaid_years_ipsi'] = df['hearingaid_years_ipsi']/1_000_000
df['hardhearing_years_ipsi'] = df['hardhearing_years_ipsi']/1_000_000
df['deaf_years_ipsi'] = df['deaf_years_ipsi']/1_000_000
df['Insertion_Angle_(IA)'] = df['Insertion_Angle_(IA)']/10

predictors = [
    'hearingaid_years_ipsi',
    'hardhearing_years_ipsi',
    'deaf_years_ipsi',
    'Insertion_Angle_(IA)',
    'mean_low_preop_AC',
    'PBmax',
    'age_atimplantation_years',
    'mean_IFT'] #Siehe Erklärung 1
"""
Erklärung 1: Ein Pandas Series Object wurde erstellt für alle Werte aus der Datei Speech_mode_2 für monosyllabic_score.
Der Score entspricht der Zielvariable und wird gegen die Variablen 'hearingaid_years_ipsi','hardhearing_years_ipsi',
'deaf_years_ipsi', 'Insertion_Angle_(IA)','mean_low_preop_AC','PBmax',
'age_atimplantation_years', 'mean_IFT' geplottet
"""

bubble_sizes = np.random.randit(50,800,size=(len(df)))

df['bubble_size'] = bubble_sizes

fig, axes = plt.subplots(nrows=2,ncols=4, figsize=(25,10))
axes = axes.flatten()

"""         
subplots ist eine Funktion des Moduls Pyplots von Matplotlib und erstellt 2x4, also 8 leere Figures/Axes mit den # angegebenen Größen 25 und 10 in Zoll.
axes.flatten ist ein Attribut von der Bibliothek numpy und wandelt multidimensionale Arrays in eindimensionale Arrays, damut über mehrere Achsen itiert werden kann ohne eingenistete For-Schleifen einsetzen zu müssen.
"""

for i, predictor in enumerate(predictors): 
    x = df[predictor]
    
    mask = ~x.isna() & ~y.isna() #Daten auf der x und y-achsen werden bereinigt, Null Werte ignoriert.
    x_clean = x[mask]
    y_clean = y[mask]

    """
    Daten auf der x und y-achsen werden bereinigt, Null Werte ignoriert
    indem eine Maske erstellt wird x.isna() gibt den Wert True zurück wenn der Wert Null ist, ~x.isna gibt True zurück wenn der Wert not Null ist.
    Diese Werte werden dann als Filter benutzt, um die gefilterte Werte zurückzugeben.

    """
    
    n = len(x_clean) #length of x_clean wurde für de

    r,p = stats.pearsonr(x_clean, y_clean) #durchführung von Person's R, Tuple Unpacking in r und p.

    slope, intercept, r_value, p_value, std_error = stats.linregress(x_clean, y_clean) # tuple unpacking in die Variablen für die Stat. Kenngrößen
    
    R_squared = round(r_value**2,4) #R² Wert auf 4 Dezimalstellen aufgerundet.
    ax = axes[i] #Die eindimensionale Achsen werden für jede Iteration in ax gespeichert damit,

    
    sns.regplot(x=x_clean, y=y_clean,ci = 95, data = df, ax = ax) #SeaBorn Kommando zur Erstellung von RegressionPlot
    sns.scatterplot(x=x_clean,y=y_clean,size='bubble_size',sizes=(50,800),alpha=0.6,color='steelblue',legend=False,data=df,ax=ax)
    
    """Zur Betitelung wurden die folgenden Anweisungen von KI erstellt"""
    
    ax.text(1.09, 0.75, f'n = {n}\nr ={r:.2f}\nR² = {R_squared:.4f}\np = {p:.3f}',
    transform = ax.transAxes, fontsize=14, verticalalignment='baseline',
    bbox=dict(boxstyle='square',facecolor = 'white', edgecolor = 'black',alpha = 1))
    
    ax.set_xlabel(predictor)
    ax.set_ylabel('monosyllabic_score')
    ax.set_title(f'{predictor} vs. monosyllabic score')
    
    if predictor == 'age_atimplantation_years':
        ax.set_ylim(y_clean.min()-10, y_clean.max() +10)
    elif predictor == 'mean_IFT':
        ax.set_xlim(0, 15)
        ax.set_ylim(y_clean.min()-10, y_clean.max() +10)
    elif predictor == 'deaf_years_ipsi':
        ax.set_xlim(-5, 60)
        ax.set_ylim(y_clean.min()-10, y_clean.max() +10)
    elif predictor == 'hearingaid_years_ipsi':
        ax.set_xlim(-5, 60)
        ax.set_ylim(y_clean.min()-10, y_clean.max() +10)
    elif predictor == 'mean_low_preop_AC':
        ax.set_xlim(0, 140)
        ax.set_ylim(y_clean.min()-10, y_clean.max() +10)
    elif predictor == 'PBmax':
        ax.set_xlim(-5,77)
        ax.set_ylim(y_clean.min()-5, y_clean.max() +10)
    elif predictor == 'Insertion_Angle_(IA)':
        ax.set_xlim(30,75)
        ax.set_ylim(y_clean.min()-5, y_clean.max() +10)
    else:
        ax.set_xlim(x_clean.min()-1, x_clean.max() +10)
        ax.set_ylim(y_clean.min(), y_clean.max() +10)
        
    
if len(predictors) < len(axes):
    for j in range(len(predictors), len(axes)):
        fig.delaxes(axes[j])

"""
Der if Block sorgt dafür, dass ungenutze figs gelöscht werden. Erstmal wird geprüft (Guard Klausel) 
"if the length of the predictors is less than the length of the axes", Wenn es mehr Achsen gibt, dann sollten alle zusätzlichen Achsen
gelöscht werden wobei "j" hier die zusätliche Achse darstellt. Dies wird dann daraufhin durch die fig.delaxes Anweisung gelöscht
"""

plt.suptitle('Monosyllabic Score - speech_mode_20250318 ', fontsize = 40) #Titel der Grafik
plt.tight_layout()
plt.show()