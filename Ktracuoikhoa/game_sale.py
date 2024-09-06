import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# check and show data
df = pd.read_csv('D:/CSA/CSA10/Ktracuoikhoa/game_sale.csv')
print(df.head(5))
print(df.shape)
print(df.columns)

# # Analyze data
fixed_df = df.loc[:, ['title','genre', 'critic_score', 'total_sales', 'na_sales', 'jp_sales','pal_sales', 'other_sales']] 
print(fixed_df.describe())

# # Top 10 bestseller games
# n = 10 
# titlelist = fixed_df['title'].value_counts().head(10).index.to_list()
# index = np.arange(n)
# width = 0.5
# xvalue = fixed_df['title'].value_counts().head(10).sort_values(ascending=True)
# bar1 = plt.barh(index, xvalue, width, color = 'green' )
# plt.ylabel('Game Title')
# plt.title('Top 10 bestseller games in 2024')

# plt.yticks(index, titlelist[::-1])
# plt.show()

# Top 10 genres 
n = 10 
titlelist = fixed_df['genre'].value_counts().head(10).index.to_list()
index = np.arange(n)
width = 0.5
xvalue = fixed_df['genre'].value_counts().head(10).sort_values(ascending=True)
bar1 = plt.barh(index, xvalue, width, color = 'green' )
plt.ylabel('Game Genres')
# Title để sao cô  
plt.yticks(index, titlelist[::-1])
plt.show()
