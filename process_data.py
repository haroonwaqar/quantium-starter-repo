import pandas as pd
import glob

data_csv_files = glob.glob("data/daily_sales_data_*.csv")

all_data = []

for file in data_csv_files:
    df = pd.read_csv(file)

    df = df[df['product'] == 'pink morsel']

    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

    df['sales'] = df['price'] * df['quantity']

    df = df[['sales', 'date', 'region']]

    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

final_df.to_csv("processed_sales_data.csv", index=False)
