import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('diabetes_datasets.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file = 'report.html')