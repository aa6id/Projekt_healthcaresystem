import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_excel(
    'C:/Users/hzhci/Desktop/speech_mode_2.xlsx')  # importiert die Daten in den Python-Interpreter

# print(df) #Kontrollanweisungn, um zu prüfen ob den DataFrame richtig und vollständig importiert wurde

# print(df.columns)

predictors = [
    'electrode_array',
    'sex',
    'deafness_course',
    'disabilities_additional_category'
]

fig, ax = plt.subplots(2, 2, figsize=(20,10)) #Mutliple SubPlots erstellt
ax = ax.flatten() #eindimensionale Numpy-Arrays erstellt

for i, predictor in enumerate(predictors): 
    sns.histplot(data=df, x=predictor, ax=ax[i]) #histplot mit den jeweiligen Parameter hierbei ist ax der Parameter der ein Histogramm für jede Iteration ax[i] erstellt
    ax[i].set_title(f'Histogram for {predictor}') #Betitelung mit Fstrings für jede Iteration von Predictors
    ax[i].set_xlabel(predictor) #Betitelung der x-Achse
    if predictor == 'disabilities_additional_category':
        ax[i].tick_params(labelrotation=45) 
        #Da die Namen der Kategorien zu groß waren, wurden mithilfe ax[i].tick_params die Labels um 45 Grad rotiert damit sie sichtbar bleiben
    else:
        ax[i].tick_params(labelrotation=0) #ansonsten keine Rotation
    ax[i].set_ylabel('Häufigkeit')



fig.suptitle(
    "Histograms for selected variables speech_mode_20250318", fontsize=40) #Betitelung der multiplen Subplots
plt.tight_layout()
plt.show()
