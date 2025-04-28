import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sklearn import preprocessing
from scipy import stats

df = pd.read_excel('O:/Dokumente/Spyder-AufG/multlinreg.xlsx')

df_use = pd.DataFrame([])

df_use['Y'] = df['hearing_loss']
df_use['X1'] = df['IA']
df_use['X2'] = df['age_atimplantation_years']

x = df_use[['X1','X2']]
y = df_use[['Y']]

# Instead of a single split, let's do k-fold cross-validation.
model = LinearRegression()

# Use cross_val_score to perform k-fold cross-validation
# By default, this will use 5-fold cross-validation, but you can adjust the number of folds using the cv parameter.
scores = cross_val_score(model, x, y.values.ravel(), cv=5, scoring='neg_mean_squared_error')

# Convert negative MSE scores to positive values
mse_scores = -scores

# Print cross-validation results
print(f"Cross-validation MSE scores: {mse_scores}")
print(f"Mean MSE from cross-validation: {mse_scores.mean():.2f}")
print(f"Standard deviation of MSE: {mse_scores.std():.2f}")

# Now you can fit the model on the full dataset and evaluate it
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_pred_series = pd.Series(y_pred.flatten(), name='Vorhergesagter Hörerhalt')
y_test_series = pd.Series(y_test.values.flatten(), name='Tatsächlicher Hörerhalt')

n = len(y_pred_series)

r, p = stats.pearsonr(y_pred_series, y_test_series)

slope, intercept, r_value, p_value, std_error = stats.linregress(y_pred_series, y_test_series)

R_squared = round(r_value**2, 4)

plt.text(70, 60, f'n = {n}\nr ={r:.2f}\nR² = {R_squared:.3f}\np = {p:.5f}', fontsize=12, verticalalignment='baseline',
bbox=dict(boxstyle='square', facecolor='white', edgecolor='black', alpha=1))

# Calculate SST, SSR, and SSE
y_test_mean = y_test_series.mean()

SST = np.sum((y_test_series - y_test_mean) ** 2)
SSR = np.sum((y_pred_series - y_test_mean) ** 2)
SSE = np.sum((y_test_series - y_pred_series) ** 2)

print(f"SST (Total Sum of Squares): {SST:.2f}")
print(f"SSR (Regression Sum of Squares): {SSR:.2f}")
print(f"SSE (Error Sum of Squares): {SSE:.2f}")

sns.regplot(x=y_pred_series, y=y_test_series, line_kws={"color": "black", "linestyle": "--"}, truncate=False)
plt.xlim(0,100)
plt.ylim(0,100)

plt.xlabel('Vorhergesagter Hörerhalt')
plt.ylabel('Tatsächlicher Hörerhalt')

plt.title('Predicted vs Actual Values')
plt.savefig("O:/Dokumente/Spyder-AufG/name.png", dpi=300, bbox_inches="tight")
plt.show()
