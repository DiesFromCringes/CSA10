import pandas as pd

df = pd.read_excel('Lab10\provinces.xls')

# rs = "List of provinces and cities: " + ", ".join([i for i in df.loc[:, "Name"]])
# print(rs)

# rs = "List of  cities: " + ", ".join([i for i in df.loc[:, "Name"]])
# print(rs)

# cities_df1 = df[df[:, 'Division'] == 'Thanh pho Trung uong', ['Name, Region']]
# print(cities_df1)

# cities_df = df[df[:, 'Division'] == 'Thanh pho Trung uong']
# print(cities_df.loc[:, ['Name', 'Region']])

# regions_count = df["Region"].value_counts()
# print(regions_count)
# max_pop = df['Population']
max_pop = df['Population'].max()
min_pop = df['Population'].min()

max_pop_province = df[df['Population'] == max_pop].iloc[0, :]
min_pop_province = df[df['Population'] == min_pop].iloc[0, :]

print(max_pop_province['Name'], str(int(max_pop_province["Population"]*1000)))
print(min_pop_province['Name'], str(int(min_pop_province["Population"]*1000)))
regions_count = df["Region"].value_counts()

area_list = []
for r in regions_count.index:
    area_list.append(df[df["Region"] == r]["Area"].sum())
total_area = df["Area"].sum()
area_proportion_list = [area / total_area * 100 for area in area_list]

# create dataframe
area_df = pd.DataFrame(
    {
        "Region": regions_count.index,
        "Total Area": area_list,
        "Area Proportion": area_proportion_list,
    }
)

print(area_df)
students_df = pd.DataFrame({
    "Name": ['Nguyen Van A', "Tran Thi B", "Lam Van C", "Nguyen Thi D", "Chau Van E"],
    "Point": [0,0,2.6,5.9,9.0], 
    "Qualify": [True, False, False, False, True]
})