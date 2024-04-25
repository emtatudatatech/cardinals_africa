import glob
import pandas as pd

from base import country_rename

# Data Key
imf_data = {
    "NGDP_RPCH": "Real GDP growth (Annual percent change)",
     "NGDPD": "GDP, current prices (Billions of U.S. dollars)",
    "PCPIEPCH": "Inflation rate, end of period consumer prices (Annual percent change)",
    "LP": "Population (Millions of people)",
    "GGXWDG_NGDP": "General government gross debt (Percent of GDP)",
     "rev": "Government revenue, percent of GDP (% of GDP)",
    "exp": "Government expenditure, percent of GDP (% of GDP)",
    "DEBT1": "DEBT (% of GDP)",
}

for key,value in imf_data.items():
    print(key, value)

# Reading all the excel files in the folder
folder = glob.glob("data\\imf_data\\*.xlsx")

for key,value in imf_data.items():
    print(f"{key}: ++++++++++++++++ {value} being extracted.")

    nations_data = []

    for file in folder:
        try:
            df = pd.read_excel(file, sheet_name = f'{key}', skiprows = [1, 3, 4])
        except Exception as e:
            print(e)
            
        df.rename(columns={f"{value}":"Nation"}, inplace = True)

        # The following are the columns we require at the end of the process
        dataset_cols = ["Nation", 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                   2021, 2022, 2023]

        df_cols = [i for i in df.columns]

        # Comparing the columns that come in with each data file to the required columns
        ds_ = set(dataset_cols)

        df_ = set(df_cols)

        diff = ds_.difference(df_)

        if len(diff) == 0:
            # Selecting the columns we need. Our time horizon for analysis is from 2013 to 2023
            sub_df = df[["Nation", 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                       2021, 2022, 2023]]
        else:
            # Adding the missing columns to the incoming data file
            for col in diff:
                df[col] = float(0)

            sub_df = df[["Nation", 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                       2021, 2022, 2023]]

        # Renaming columns
        sub_df.columns = ["Nation", '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                   '2021', '2022', '2023']

        nations_data.append(sub_df)

    dataset = pd.concat(nations_data)

    # Ensuring consistency of the names of the nations
    dataset["Nation"] = dataset["Nation"].apply(lambda x: country_rename(x))

    # Unpivoting the content to form a long dataset
    melted_dataset = pd.melt(dataset, id_vars=['Nation'], var_name='Year', value_name=f'{value}')

#     display(melted_dataset)

    # Save dataset for analysis
    melted_dataset.to_parquet(f"data\\analysis_datasets\\{value}.parquet", index = False)
    print(f"Saved {value} data")
    
    del(nations_data, df, dataset, melted_dataset)