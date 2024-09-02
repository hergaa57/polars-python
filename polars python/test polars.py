import pandas as pd
import polars as pl

df_sheet1 = pl.read_excel('gal.xlsx', sheet_name='Sheet1')
df_sheet2 = pl.read_excel('gal.xlsx', sheet_name='Sheet2')

print("Data dari sheet 1: ")
print(df_sheet1)

print("Data dari sheet 2: ")
print(df_sheet2)

joined_df = df_sheet2.join(df_sheet1, left_on='departemen_id', right_on='id', how='right')

print("\nHasil Join: ")
print(joined_df)

joined_df.write_excel('gal1.xlsx')