import json
import csv

input_file = 'ccs_synthetic_filtered_large.json'
output_file = 'ccs_synthetic_filtered_large.tsv'

with open(input_file, 'r') as f:
    data = json.load(f)

# extract header and data from JSON
header = data[0].keys()
rows = [x.values() for x in data]

# write data to TSV file
with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(header)
    writer.writerows(rows)
