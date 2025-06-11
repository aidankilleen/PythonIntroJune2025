# pandas_investigation.py

import pandas as pd


s = pd.Series([10, 20, 30])
print (s)


df = pd.DataFrame({'A':[1, 2, 3, 4], 'B':[5, 6, 7, 8], 'C':[9, 10, 11, 12]})

print (df)


df_sales = pd.read_csv("sales.csv")

#print (df_sales)
#quantities = df_sales['quantity']
#print (quantities)


pivot = pd.pivot_table(df_sales, index="product", columns="colour", values="quantity", aggfunc="sum", fill_value=0)

# add in the Totals column
pivot['totals'] = pivot.sum(axis=1)

# print (pivot)

# add in the Totals row
totals_row = pivot.sum(axis=0).to_frame().T
totals_row.index = ["Totals"]   # put "Totals" into the first column
# print (totals_row)

pivot_with_totals = pd.concat([pivot, totals_row])
print (pivot_with_totals)







