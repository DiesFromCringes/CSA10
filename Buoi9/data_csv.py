import pandas as pd
# # print(pd.__version__)
# # df = pd.read_csv('D:\CSA\CSA10\Buoi9\pokemon_data.csv')
# # print(df.head())
# # print('--------')
# # print(df.tail())

# df = pd.DataFrame(
#     {
#         'Name': ['Anastasia', 'Dima', 'Katherine'],
#         'Score': [12.5, 9.0, 16.5],
#         'Attemps': [1, 3, 2],
#     }
# )
# print(df)
# df.to_csv('new.csv')

# ve du lieu len bang do (cho so - 2D)
import matplotlib.pyplot as plt

df = pd.read_csv('D:\CSA\CSA10\Buoi9\pokemon_data.csv')
plt.figure(figsize=(10, 6))

plt.plot(df['HP'], df['Attack'], marker='o')
plt.title('HP va Attack')
plt.ylabel('Attack')
plt.xlabel('HP')

plt.grid(True)
plt.show()