# countplot

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks', color_codes=True)

x = sns.load_dataset('titanic')

p = sns.countplot(x = 'sex' , data= x, hue='class')
p.set_title('Plot')
plt.show()
