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
sold.to_csv('all_property_type_sold.csv', index=False)

sold = sold[sold['PropertyType'] == 'Residential']
print(len(sold))
print(sold["PropertyType"].unique())

sold.to_csv('combined_sold.csv', index=False)
print("successful")

# find all the LISTING files
all_listing = []
for f in files:
    if f.startswith('CRMLSListing'):
        all_listing.append(f)

# list all the normal version and filled version files in LISTING files
normal_listing = []
for f in all_listing:
    if not f.endswith('_filled.csv'):
        normal_listing.append(f)

filled_listing = []
for f in all_listing:
    if f.endswith('_filled.csv'):
        filled_listing.append(f)

# keep the filled version
files_listing = []
for f in filled_listing:
    files_listing.append(f)

for f in normal_listing:
    filled_name = f.replace('.csv', '_filled.csv')
    if filled_name not in filled_listing:
        files_listing.append(f)

print(len(files_listing))

# store all the listing files into listing_dfs
listing_dfs = []
for i in files_listing:
    df = pd.read_csv("/workspaces/IDX_Summer_2026/csv/" + i)
    listing_dfs.append(df)

# concatenate all listing files
listings = pd.concat(listing_dfs)
print(listings.shape)
listings.to_csv('all_property_type_listings.csv', index=False)

# filter Residential only
listings = listings[listings['PropertyType'] == 'Residential']
print(len(listings))

# save
listings.to_csv('combined_listings.csv', index=False)
print("successful")