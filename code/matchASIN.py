import pandas as pd
import json

# Load the CSV data into a DataFrame
def load_csv_data(csv_file_path):
    # Skip the first row (header) and set column data types
    df = pd.read_csv(csv_file_path, skiprows=1, dtype={'0': str, '1': int}, header=None)
    df.columns = ['asin', 'count']  # Rename columns for clarity
    return df

# Process the JSON file to match ASINs and extract required data
def process_json_file(json_file_path, asins):
    asin_data = {}
    with open(json_file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):  # Start enumeration at 1 for line numbers
            try:
                item = json.loads(line)
                if item.get('asin') in asins:
                    # Handle missing keys and structure variations
                    title = item.get('title', 'N/A')
                    category = item.get('category', ['N/A'])
                    #rank = item.get('rank', 'N/A').split(' in ')[0] if 'rank' in item and item['rank'] else 'N/A'  # Extract rank number
                    rank = item.get('rank', 'N/A')
                    asin_data[item['asin']] = {'title': title, 'category': category, 'rank': rank}
            except json.JSONDecodeError:
                print(f"Warning: Skipping badly formatted line {line_number}.")
    return asin_data

# Combine CSV data with JSON extracted data and write to a new CSV
def combine_data_and_write_csv(csv_data, json_data, output_csv_path):
    combined_data = []
    for index, row in csv_data.iterrows():
        asin = row['asin']
        review_count = row['count']
        if asin in json_data:
            meta = json_data[asin]
            combined_data.append({
                'asin': asin,
                'review_count': review_count,
                'title': meta['title'],
                'category': ', '.join(meta['category']),
                'rank': meta['rank']
            })
    output_df = pd.DataFrame(combined_data)
    output_df.to_csv(output_csv_path, index=False)

# Main function to orchestrate the process
def process_asin_data(csv_file_path, json_file_path, output_csv_path):
    # Load CSV data
    csv_data = load_csv_data(csv_file_path)

    # Process JSON and match with CSV ASINs
    json_data = process_json_file(json_file_path, set(csv_data['asin']))

    # Combine and write to new CSV
    combine_data_and_write_csv(csv_data, json_data, output_csv_path)

# Define file paths (you need to replace these with your actual file paths)
csv_file_path = 'asin_reviews_counts.csv'
json_file_path = 'meta_Books.json'
output_csv_path = 'combined_data.csv'

# Run the main function
process_asin_data(csv_file_path, json_file_path, output_csv_path)
