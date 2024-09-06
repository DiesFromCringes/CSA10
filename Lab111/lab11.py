import pandas as pd
from google.colab import drive
border_file ='/content/borders.xls'
coastline_file = '/content/coastlines.xls'
province_file ='/content/provinces.xls'
border_df = pd.read_excel(border_file)
print(border_df.tail(3))
coastline_df = pd.read_excel(coastline_file)
print(coastline_df.tail(3))
province_df = pd.read_excel(province_file)
print(province_df.tail(3))
"""
**Bai 2: Bo bien**
"""
print('Number of provinces & cities with coastline:',len(coastline_df))
# Gop du lieu vao bang province
coastlines = []
# chay vong lap trong province de lay du lieu cho list coastlines
for name in province_df['Name']:
  matching_row = coastline_df[coastline_df['Name'] == name]
  if not matching_row.empty:
    # co du lieu ve duong bo bien
    coastlines.append(matching_row['Coastline'].iat[0])
  else:
    # khong co du lieu ve duong bo bien
    coastlines.append(0)
  #them cot coastline vao bang province
province_df['Coastline'] = coastlines
print(province_df)
province_df.to_excel('provinces_updated.xlsx', index=False)
"""**Bai 3: Bien gioi**"""
# tao bang border_updated rieng
border_updated_df = pd.DataFrame(columns=['Name', 'BorderWith', 'BorderCount'])
# chay file de doc data trong tung sheet
border_list = (('CHN', 'China'), ('LAO', 'Laos'), ('KHM', 'Combodia'))
for coutry in border_list:
  inp_df = pd.read_excel(border_file, sheet_name=coutry[0])
# chay vong lap de ghi vao file province
  for name in inp_df['Tên tỉnh']:
    matching_row = border_updated_df[province_df['Name'] == name]
    if(not matching_row.empty):
      border_updated_df.at[matching_row.index[0], 'BorderWith'] += ", " + coutry[1]
      border_updated_df.at[matching_row.index[0], 'BorderCount'] += 1
    else:
      border_updated_df = pd.concat([border_updated_df, pd.DataFrame({'Name': [name], 'BorderWith': [coutry[1] + ','], 'BorderCount': [1]})], ignore_index=True)
# in ra bang province
print(border_updated_df)
# update du lieu cho file province
border_updated_df.to_excel("borders_updated.xlsx", index=False)
