import pandas as pd

# Excel file load karo
df = pd.read_excel("data.xlsx")

# Duplicate rows remove
df = df.drop_duplicates()

# Sort by first column
df = df.sort_values(df.columns[0])

# Cleaned file save
df.to_excel("cleaned_data.xlsx", index=False)

print("Excel cleaned and saved successfully!")
