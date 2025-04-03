import numpy as np
import  pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_excel(
    'C:/Users/hzhci/Desktop/speech_mode_2.xlsx') #importiert die Daten in den Python-Interpreter

# print(df) Kontrollanweisungn, um zu prüfen ob den DataFrame richtig und vollständig importiert wurde

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

#print(df.dtypes) 
#Kontrollanweisung, um zu prüfen ob die Datentypen float oder int sind damit die Berechnungen durchführbar sind


fig, axes = plt.subplots(2, 4, figsize=(25,10))
axes.flatten()
    


#subplots ist eine Funktion des Moduls Pyplots von Matplotlib und erstellt 2x4, also 8 leere Figures/Axes mit den
#angegebenen Größen 25 und 10 in Zoll

for i, predictor in enumerate(predictors): 
    x = df[predictor] #entspricht jeden Wert in Predictor, wird dann in x_clean als bereinigte Daten gespeichert
    
#eine For-Scheife die über die Werte der Liste Predictors itiert, damit eine Grafik für jeden Predictor mit dem
#folg. Code erstellen lässt.

    mask = ~x.isna() & ~y.isna() #Daten auf der x und y-achsen werden bereinigt, Null Werte ignoriert.
    x_clean = x[mask]
    y_clean = y[mask]


    n = len(x_clean) #length of x_clean wurde für de

    r,p = stats.pearsonr(x_clean, y_clean) #durchführung von Person's R, Tuple Unpacking in r und p.

    slope, intercept, r_value, p_value, std_error = stats.linregress(x_clean, y_clean)
    #linear regression für x_clean and y_clean, nochmal tuple unpacking in die obigen Variablen

    line = slope * x_clean + intercept #Linie mit den Werten aus Zeile 56.

    R_squared = r_value**2 #Wert für R_Squared
    
    ax = axes[i]

    #g = sns.relplot(data=df, x= x_clean, y =y_clean)
    sns.regplot(x= x_clean, y= y_clean, data = df, ax = ax)
    #scatter = ax.scatter(x_clean, y_clean, s = 20, color = "blue", alpha = 0.7)
    #Erstellung des Scatterplots -hierzu noch mehr Modifikationen für die Anzahl/Häufigkeitsberechnung
    
    #x_sorted = np.sort(x_clean)
    #y_fit = slope * x_sorted + intercept
    
    

#ax.plot(x_sorted, y_fit, color = "blue", linestyle='solid')
    
   # ab diesem Punkt wurde künstliche Intelligenz in Anspruch genommen

    #ax.text(1.09, 0.75, f'n = {n}\nr ={r:.2f}\nR² = {R_squared:.2f}\np = {p:.3f})',
    #transform = ax.transAxes, fontsize=12, verticalalignment='baseline',
    #bbox=dict(boxstyle='square',facecolor = 'white',alpha = 1))

    #ax.set_xlabel(predictor)
    #ax.set_ylabel('monosyllabic_score')
    #ax.set_title(f'{predictor} vs. monosyllabic score')
    
if len(predictors) < len(axes):
    for j in range(len(predictors), len(axes)):
        fig.delaxes(axes[j])
        
        

plt.tight_layout()
plt.show()