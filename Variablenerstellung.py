import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn.linear_model import LinearRegression


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn.linear_model import LinearRegression


df = pd.read_excel('O:/Dokumente/Spyder-AufG/speech_model_data_baseline (13).xlsx') 


df['hearing_impaired_years2'] = df[['hardhearing_years','deaf_years']].max(axis=1)

df.to_excel('O:/Dokumente/Spyder-AufG/speech_model_data_baseline (13).xlsx', index = False)
