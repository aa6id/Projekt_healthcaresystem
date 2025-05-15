import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('O:/Docs/D13_Daten.xlsx')


y_werte = ['diff_estimated_real', 'diff_predicted_real']  
x = df['monosyllabic_score']


boxplot_data = pd.melt(df, id_vars=["monosyllabic_score"], value_vars=y_werte, 
                       var_name="Difference in Monosyllabic Score", value_name="Difference")
#test 
#print(boxplot_data)

fig, ax = plt.subplots(2, 1, figsize=(10, 10))

sns.scatterplot(x=x, y=df[y_werte[0]], ax=ax[0], color='cadetblue', label="Estimated", marker='o', s=100)
sns.scatterplot(x=x, y=df[y_werte[1]], ax=ax[0], color='steelblue', label="Predicted", marker='o', s=100)

ax[0].set_title('Scatterplot of differences between estimated and predicted monosyllabic scores')
ax[0].set_xlabel('Monosyllabic Score (%)', fontsize=15)
ax[0].set_ylabel(r'$\mathrm{MS_{pred} - MS_{ref}}$ [°]', fontsize=15)
ax[0].set_xlim(0,100)
ax[0].yaxis.grid(True, linestyle='--', linewidth=0.9, alpha=0.9)
ax[0].legend(title='LEGENDE')

box = sns.boxplot(data=boxplot_data, x="Difference in Monosyllabic Score", y="Difference", palette=("cadetblue","steelblue"), ax=ax[1])


ax[1].set_title('Combined Boxplot of the differences between estimated and predicted monosyllabic scores')
ax[1].set_ylabel(r'$\mathrm{MS_{pred} - MS_{ref}}$ [°]', fontsize=15)
plt.xticks(ticks=[0, 1], labels=['Estimated', 'Predicted',])


plt.tight_layout()
plt.savefig("O:/Docs/grafik_final.jpg", dpi=300, bbox_inches="tight")
plt.show()
