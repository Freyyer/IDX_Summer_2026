import pandas as pd

sold=pd.read_csv("/workspaces/IDX_Summer_2026/all_property_type_sold.csv")
listings=pd.read_csv("/workspaces/IDX_Summer_2026/all_property_type_listings.csv")
print(sold.head(10))
print(sold.shape)
print(listings.head(10))
print(listings.shape)

#it seems like there are some columns with same names like "livingArea" and "livingArea.1". I'm not sure how to deal with it.
print(listings.columns)
print(sold.columns)

#the filtering logic applied
print(sold['PropertyType'].unique())
print(listings['PropertyType'].unique())

# Null-count summary table
nulls_counts_sold=sold.isnull().sum()
print(nulls_counts_sold)

nulls_counts_listings=listings.isnull().sum()
print(nulls_counts_listings)

null_percent_sold = sold.isnull().sum() / sold.shape[0] * 100
null_percent_listings = listings.isnull().sum() / listings.shape[0] * 100

def flagging(form):
    flagging_column=[]
    for idx, val in form.items():
        if val > 90:
            flagging_column.append(idx)
    return flagging_column

flagging_column_sold=flagging(null_percent_sold)
flagging_column_listings=flagging(null_percent_listings)
print(flagging_column_sold)
print(flagging_column_listings)

sold = sold.drop(columns=flagging_column_sold)
listings = listings.drop(columns=flagging_column_listings)

#filter to only “residential”
sold_residential = sold[sold["PropertyType"]=="Residential"]
listings_residential = listings[listings["PropertyType"]=="Residential"]

print(len(sold_residential))
print(len(listings_residential))

print(sold_residential[['ClosePrice', 'LivingArea', 'DaysOnMarket']].describe())
print(listings_residential[['ClosePrice', 'LivingArea', 'DaysOnMarket']].describe())


sold_residential.to_csv('drop_sold.csv', index=False)
listings_residential.to_csv('drop_listings.csv', index=False)