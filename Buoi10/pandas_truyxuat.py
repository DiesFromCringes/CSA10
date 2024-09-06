import pandas as pd
df = pd.read_excel('D:/CSA/CSA10/Buoi10/pokemon_data.xlsx')
# data = df.Name
# data = df['HP']
# print(data.head(10))
# print(type(data))
# data = df[4:30:5]
# print(data)
# print(type(data))
# data = df[["Name", "HP"]]
# print(data.head(3))
# print(type(data))
# data = df.iloc[:, 'Name']
# print(data.head(3))
# print(type(data))
# data = df.iloc[10, 'HP']
# print(data)
# print(type(data))
# data = df.iloc[:, 'HP':'Speed']
# print(data.head(2))
# data = df.iloc[:, ['HP','Speed']]
# print(data.head(2))
# print(df.iloc[5:50:10, ['HP','Attack']])
# data = df.iiloc[;, 1]
# print(data.head(3))
# print(type(data))
# data = df.iloc[10, 3 ]
# print(data)
# print(type(data))
# # nhieu cot => dataFrame
# data = df.iloc[:, 1:5]  # lay lien tuc
# print(data.head(2))
# data = df.iloc[:, [5, 11]] # lay tung cot cu the
# print(data.head(2))
# data = df.iloc[1:3]
# print(data)
# # nhieu cot + nhieu hang 
# print(df.iloc[5:50:10, [9, 10]])
# print(df['HP'].describe())
# print('sum', df.HP.sum())
# print('value counts', df.Legendary.value_counts())
# filtered_df = df.HP > 150
# print(filtered_df)
filtered_df = df[df.Name == "Chansey"]
print(filtered_df)
