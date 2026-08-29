import pandas as pd

# Sample DataFrame
sample_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
})


sample_df['Name2'] = sample_df['Name'] + ' Smith'  # Adding a new column with modified names
print(sample_df)