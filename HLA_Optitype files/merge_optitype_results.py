import pandas as pd
import os
from glob import glob

# Root directory where all sample folders are stored
root_dir = "/mnt/d/practice/allfils_hla"

# Collect all result.tsv files recursively
tsv_files = glob(os.path.join(root_dir, "*/*/*_result.tsv"))

dataframes = []
for f in tsv_files:
    try:
        # Extract sample ID (parent folder name)
        sample_id = f.split('/')[-3]
        df = pd.read_csv(f, sep='\t')
        df.insert(0, 'Sample_ID', sample_id)
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {f}: {e}")

# Combine all data
final_df = pd.concat(dataframes, ignore_index=True)

# Clean up extra whitespace in headers
final_df.columns = final_df.columns.str.strip()

# Save to Excel
output_file = os.path.join(root_dir, "OptiType_merged_results.xlsx")
final_df.to_excel(output_file, index=False)

print(f"✅ Merged Excel file created at: {output_file}")
