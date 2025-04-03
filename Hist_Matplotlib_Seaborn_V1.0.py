import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_excel(
    'C:/Users/hzhci/Desktop/speech_mode_2.xlsx')  # importiert die Daten in den Python-Interpreter

# print(df) #Kontrollanweisungn, um zu prüfen ob den DataFrame richtig und vollständig importiert wurde

print(df.columns)

predictors = [
    'PBmax',
    'monosyllabic_score',
    'sex',
    'deafness_course',
    'age_atimplantation_years',
    'implant_usage_years',
    'hardhearing_years_ipsi',
    'deaf_years_ipsi',
    'hearingaid_years_ipsi',
    'mean_IFT',
    ]



for i, predictor in enumerate(predictors):
    g = sns.FacetGrid(df, col = predictor)
    g.map(sns.histplot)
"""
    x.hist(ax=axes[i],
           edgecolor = 'white',
           color = 'blue'
           )
    axes[i].set_title(f'{predictor} distribution')
    axes[i].set_xlabel(predictor)
    axes[i].set_ylabel('Häufigkeit')
"""
plt.tight_layout()
plt.show() 