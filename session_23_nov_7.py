# import csv

# read_csv = csv.reader(open('realistic_customers_with_issues.csv'))

# for row in read_csv:
#     #print(row)
#     for column_index in range(len(row)):
#         print(row [column_index])
#         if row[column_index] != '':
#             print(row)
    
#     print('\n')

import pandas as pd

df = pd.read_csv('realistic_customers_with_issues.csv')

for index, row in df.iterrows():
    # print(index)
    # print(row)
    print(df)
    print(df.loc[index])


print(df.columns)
print(df['name'].value_counts())

missing_values = df[df.isnull().any(axis=1)]
print(missing_values)

df = df.dropna()

# print(df)

duplicates = df[df.duplicated(subset='id',keep=False)]



print(duplicates)

problematic_rows = pd.concat([missing_values,duplicates]).drop_duplicates

print(problematic_rows_df)


problematic_rows_df.to_csv('my_data_problems.csv', index=False)

email_placeholder = "no email"

problematic_rows_df['email']=problematic_rows_df['email'].fillname
problematic_rows_df.to_csv('my_data_w_less_problems.py')


















