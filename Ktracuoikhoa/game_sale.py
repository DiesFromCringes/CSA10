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

# # top 10 games have highest total sales (wholeworld) (all versions)
# group_by_title_df = fixed_df.groupby('title').sum()
# group_by_title_df= group_by_title_df.sort_values(by='total_sales', ascending=False).head(10)

# # ve bieu do cot ngang 
# plt.barh(group_by_title_df.index[::-1], group_by_title_df['total_sales'][::-1], 0.5, color='green')
# plt.xlabel('Total Sales')
# plt.ylabel('Title')
# plt.show()


# # top 10 games genre have highest total sales (wholeworld) (all versions)
# group_by_title_df = fixed_df.groupby('genre').sum()
# group_by_title_df= group_by_title_df.sort_values(by='total_sales', ascending=False).head(10)

# # ve bieu do cot ngang 
# plt.barh(group_by_title_df.index[::-1], group_by_title_df['total_sales'][::-1], 0.5, color='green')
# plt.xlabel('Total Sales')
# plt.ylabel('Title')
# plt.show()


# top 10 games genre have highest critic score (wholeworld) (all versions)
# group_by_title_df = fixed_df.groupby('genre').sum()
# group_by_title_df= group_by_title_df.sort_values(by='total_sales', ascending=False).head(10)

# # ve bieu do cot ngang 
# plt.barh(group_by_title_df.index[::-1], group_by_title_df['total_sales'][::-1], 0.5, color='green')
# plt.xlabel('Total Sales')
# plt.ylabel('Title')
# plt.show()

# # top 10 games have highest critic score (avg/ version)
# highest_score_df = fixed_df.loc[:, ['title', 'critic_score']].groupby('title').mean()
# highest_score_df= highest_score_df.sort_values(by='critic_score', ascending=False).head(10)
# # ve bieu do cot ngang 
# plt.barh(highest_score_df.index[::-1], highest_score_df['critic_score'][::-1], 0.5, color="green")
# plt.xlabel('Critic score')
# plt.ylabel('Title')
# plt.show()

# mối tương quan giữa critic score và total sales
# plt.scatter(fixed_df['critic_score'], fixed_df['total_sales'], color="green")
# plt.xlabel('Critic score')
# plt.ylabel('Total sales')
# plt.show()

# # top 10 games have highest critic score (avg/ version)
# highest_score_df = fixed_df.loc[:, ['title', 'critic_score']].groupby('title').mean()
# highest_score_df= highest_score_df.sort_values(by='critic_score', ascending=False).head(10)
# # ve bieu do cot ngang 
# plt.barh(highest_score_df.index[::-1], highest_score_df['critic_score'][::-1], 0.5, color="green")
# plt.xlabel('Critic score')
# plt.ylabel('Title')
# plt.show()

# top 10 genres have highest total sales (wholeworld) (all versions)
group_by_title_df = fixed_df.groupby('genre').sum()
group_by_title_df= group_by_title_df.sort_values(by='total_sales', ascending=False)
# ve bieu do cot ngang 
plt.pie( group_by_title_df['total_sales'][::-1], labels=group_by_title_df.index[::-1], autopct='%1.1f%%')
plt.show()
# plt.legend(loc="best")
plt.show()