import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel('O:/Docs/D13_Daten.xlsx')

# Define variables
y_werte = ['diff_estimated_real', 'diff_predicted_real']  
x = df['monosyllabic_score']

# Reshape the data for the combined boxplot
boxplot_data = pd.melt(df, id_vars=["monosyllabic_score"], value_vars=y_werte, 
                       var_name="Measurement", value_name="Difference")

# Set up subplots: one row for scatter plots, one row for boxplots
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Scatter plot combined into one
sns.scatterplot(x=x, y=df[y_werte[0]], ax=ax[0], color='darkblue', label=y_werte[0], marker='o')
sns.scatterplot(x=x, y=df[y_werte[1]], ax=ax[0], color='steelblue', label=y_werte[1], marker='o')

# Title and labels for the scatter plot
ax[0].set_title('Scatterplot of diff_estimated_real and diff_predicted_real')
ax[0].set_xlabel('Monosyllabic Score (%)', fontsize=15)
ax[0].set_ylabel(r'$\mathrm{MS_{pred} - MS_{ref}}$ [°]', fontsize=15)
ax[0].legend(title='LEGENDE')

# Boxplot
sns.boxplot(data=boxplot_data, x="monosyllabic_score", y="Difference", hue="Measurement", ax=ax[1])

# Title and labels for the boxplot
ax[1].set_title('Combined Boxplot of diff_estimated_real and diff_predicted_real')
ax[1].set_xlabel('Monosyllabic Score (%)', fontsize=15)
ax[1].set_ylabel(r'$\mathrm{MS_{pred} - MS_{ref}}$ [°]', fontsize=15)

# Adjust layout for better spacing between plots
plt.tight_layout()

# Show the plots
plt.show()
