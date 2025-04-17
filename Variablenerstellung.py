import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn.linear_model import LinearRegression


df = pd.read_excel('O:/Dokumente/Spyder-AufG/speech_model_data_baseline (13).xlsx') 


y = df['monosyllabic_score']

print(df)

"""
when deaf_years is true and when hard_hearing_years is true
 then assign to deaf years
 
when deaf years is None but hard_hearing_years is true
 then assign to hard_hearing_years
 """


df['hearing_impaired_years'] = None


for index, row in df.iterrows():
    if row['deaf_years'] is not None:
        df.at[index, 'hearing_impaired_years'] = row['deaf_years']
    elif row['hardhearing_years'] is not None:
        df.at[index, 'hearing_impaired_years'] = row['hardhearing_years']
        
df["hearing_impaired_years"]