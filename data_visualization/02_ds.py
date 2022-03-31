#count plot

import pandas as pd

df = pd.read_csv('Sample - Superstore_Orders.csv')

print(df)


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks', color_codes=True)


p = sns.countplot (x = 'Category' , data= df)
p.set_title('Plot')
plt.show()
