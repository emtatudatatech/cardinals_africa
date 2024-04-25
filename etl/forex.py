import pandas as pd
import glob

from base import country_rename

# Reading all the excel files in the folder
folder = glob.glob("data\\forex_raw\\*.csv")

forex_columns = ["Date", "Price", "Change %", "Nation"]

forex_data = []

for file in folder:
    try:
        df = pd.read_csv(file, usecols = forex_columns, parse_dates = ["Date"], infer_datetime_format = True)
        df.rename(columns={"Change %":"Change"}, inplace = True)
        forex_data.append(df)

    except Exception as e:
        print(e)

dataset = pd.concat(forex_data)

# Ensuring consistency of the names of the nations
dataset["Nation"] = dataset["Nation"].apply(lambda x: country_rename(x))

print(dataset.info())

# Save dataset for analysis
dataset.to_csv("data\\analysis_datasets\\forex_data.csv", index = False, header = True)
print(f"Saved data")

del(forex_data, df, dataset)