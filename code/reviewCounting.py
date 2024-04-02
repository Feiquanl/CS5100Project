import json
import csv

asin_counts = {}

# Open your JSON file
with open('Books_5.json', 'r', encoding='utf-8') as file:
    # Process each line in the file
    for line in file:
        # Convert the line from a JSON string to a dictionary
        record = json.loads(line)
        
        # Extract the ASIN from the record
        asin = record['asin']
        
        # Increment the count for this ASIN
        asin_counts[asin] = asin_counts.get(asin, 0) + 1

# Print the count of items for each ASIN
#for asin, count in asin_counts.items():
#    print(f"ASIN: {asin}, Count: {count}")

with open('asin_counts.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header row
    writer.writerow(['ASIN', 'Count'])
    
    # Write the counts for each ASIN
    for asin, count in asin_counts.items():
        writer.writerow([asin, count])

print("ASIN counts have been written to asin_counts.csv.")
