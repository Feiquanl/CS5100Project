import pandas as pd
import json

# Placeholder for the records with the specified ASIN
filtered_records = []

# The ASIN you're looking for
target_asin = '0001713353'

# Assuming you have a JSON file, replace 'your_json_file.json' with your actual file path
with open('Books_5.json', 'r', encoding='utf-8') as file:
    # Load JSON records one by one
    for line in file:
        record = json.loads(line)
        if record['asin'] == target_asin:
            filtered_records.append(record)

# Create a DataFrame from the filtered records
df = pd.DataFrame(filtered_records)

# Write the DataFrame to an Excel file
excel_filename = 'filtered_data.xlsx'
df.to_excel(excel_filename, index=False)
