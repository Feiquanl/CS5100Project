import pandas as pd
import json

# Placeholder for the records with the specified ASIN
filtered_records = []

# The ASIN you're looking for
target_asin = ["0385376715", "038538369X", "0375813616", "0374300216",
"0887431453", "1419708457", "1609580834", "0811877825", "0763644765",
"1609580427", "0439358078", "0803731930"]

# Assuming you have a JSON file, replace 'your_json_file.json' with your actual file path
with open('Books_5.json', 'r', encoding='utf-8') as file:
    # Load JSON records one by one
    for line in file:
        record = json.loads(line)
        if record['asin'] in target_asin:
            filtered_records.append(record)

# Create a DataFrame from the filtered records
df = pd.DataFrame(filtered_records)

# Write the DataFrame to an Excel file
#excel_filename = "extractedReviews/Book_1_12.csv"
#df.to_excel(excel_filename, index=False)

csv_filename = "extractedReviews/Book_1_12.csv"
df.to_csv(csv_filename, index=False)