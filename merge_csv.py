import pandas as pd

# Read both CSV files
df1 = pd.read_csv('restos (1).csv')
df2 = pd.read_csv('restos_2025.csv')

# Concatenate the dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('FoodpandaCombo.csv', index=False)
print("CSV files merged successfully!")
