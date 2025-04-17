import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn.linear_model import LinearRegression


df = pd.read_excel('O:/Dokumente/Spyder-AufG/speech_model_data_baseline (13).xlsx') 


y = df['monosyllabic_score']



predictors = [
    'hearingaid_usage_years',
    'hardhearing_years',
    'deaf_years',
    'IA',
    'low_freq_preop_mean',
    'PBmax',
    'age_atimplantation_years',
    'mean_IFT',
    'hearing_impaired_years'
]



fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(25, 10))
axes = axes.flatten()

for i, predictor in enumerate(predictors):
    x = df[predictor]
    
    
    mask = ~x.isna() & ~y.isna()
    x_clean = x[mask]
    y_clean = y[mask]
    
    n = len(x_clean)

    
    r, p = stats.pearsonr(x_clean, y_clean)

    
    slope, intercept, r_value, p_value, std_error = stats.linregress(x_clean, y_clean)

    
    R_squared = round(r_value**2, 4)
    
    
    lin_reg = LinearRegression()
    lin_reg.fit(x_clean.values.reshape(-1, 1), y_clean)
    y_pred = lin_reg.predict(x_clean.values.reshape(-1, 1))
    
    
    df_plot = pd.DataFrame({
    "x": x_clean,
    "y": y_clean
    })

    
    df_plot["size"] = df_plot.groupby(["x", "y"])["x"].transform("count")

    ax = axes[i]
    sns.regplot(x=x_clean, y=y_pred, data=df_plot, ax=ax)
    sns.scatterplot(x=x_clean, y=y_clean, size='size', sizes=(50, 800), alpha=0.6, color='steelblue', legend=False, data=df_plot, ax=ax)
    
    ax.text(1.03, 0.63, f'n = {n}\nr ={r:.2f}\nR² = {R_squared:.3f}\np = {p:.3f}',
            transform=ax.transAxes, fontsize=12, verticalalignment='baseline',
            bbox=dict(boxstyle='square', facecolor='white', edgecolor='black', alpha=1))
    
    ax.set_xlabel(predictor)
    ax.set_ylabel('monosyllabic_score')
    ax.set_title(f'{predictor} vs. monosyllabic score')
    
    
    if predictor == 'hearingaid_usage_years':
        ax.set_xlim(-5, 90)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    elif predictor == 'hardhearing_years':
        ax.set_xlim(-5, 90)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    elif predictor == 'deaf_years':
        ax.set_xlim(-5, 90)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    elif predictor == 'hearingaid_years_ipsi':
        ax.set_xlim(-5, 90)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    elif predictor == 'low_freq_preop_mean':
        ax.set_xlim(-10, 140)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    elif predictor == 'PBmax':
        ax.set_xlim(-5, 100)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    elif predictor == 'IA':
        ax.set_xlim(290, 750)
        ax.set_ylim(y_clean.min() - 5, y_clean.max() + 10)
    elif predictor == 'hearing_impaired_years':
        ax.set_xlim(-5, 90)
        ax.set_ylim(y_clean.min() - 10, y_clean.max() + 10)
    else:
        ax.set_xlim(x_clean.min() - 1, x_clean.max() + 10)
        ax.set_ylim(y_clean.min(), y_clean.max() + 10)


if len(predictors) < len(axes):
    for j in range(len(predictors), len(axes)):
        fig.delaxes(axes[j])


plt.suptitle('Monosyllabic Score - speech_model_data_baseline', fontsize=40)
plt.tight_layout()
plt.show()
