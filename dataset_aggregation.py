import pandas as pd
import os

files=os.listdir("/workspaces/IDX_Summer_2026/csv")


# find all the SOLD files
all_sold = []
for f in files:
    if f.startswith('CRMLSSold'):
        all_sold.append(f)

# list all the normal version and filled version files in SOLD files
normal = []
for f in all_sold:
    if not f.endswith('_filled.csv'):
        normal.append(f)

filled = []
for f in all_sold:
    if f.endswith('_filled.csv'):
        filled.append(f)

print("normal version:", sorted(normal))
print("filled version:", sorted(filled))

#keep the filled version
files_sold = []
for f in filled:
    files_sold.append(f)


for f in normal:
    filled_name = f.replace('.csv', '_filled.csv')
    if filled_name not in filled:
        files_sold.append(f)

print(sorted(files_sold))
print(len(files_sold))

# store all the 29 files into sold.dfs 
sold_dfs = []
for i in files_sold:
    df = pd.read_csv("/workspaces/IDX_Summer_2026/csv/" + i)
    sold_dfs.append(df)

#concatenate all the 29 files in SOLD 
sold = pd.concat(sold_dfs)
print(len(sold))
print(sold.head())
print(sold.shape)

print(sold.columns)

normal_df = pd.read_csv("/workspaces/IDX_Summer_2026/csv/CRMLSSold202401.csv")
filled_df = pd.read_csv("/workspaces/IDX_Summer_2026/csv/CRMLSSold202401_filled.csv")

print("normal column:", len(normal_df.columns))
print("filled column:", len(filled_df.columns))

# find the columns that exist in filled version but not in normal version
extra_cols = [c for c in filled_df.columns if c not in normal_df.columns]
print("extra column:", extra_cols)

sold = sold.drop(columns=['latfilled', 'lonfilled'])
print(sold.shape)

print(sold["PropertyType"].unique())

sold = sold[sold['PropertyType'] == 'Residential']
print(len(sold))
print(sold["PropertyType"].unique())

sold.to_csv('combined_sold.csv', index=False)
print("successful")