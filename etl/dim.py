import pandas as pd

africa = pd.read_csv("data\\africa_raw.csv", converters = {'Next_Election_Year': str})

dim_africa = africa[["Nation", "Country_Code", "Next_Election_Year", "Region"]]

dim_africa.to_parquet("data\\analysis_datasets\\dim_africa.parquet", index = False)