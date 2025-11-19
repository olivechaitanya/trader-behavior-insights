"""
Create a smaller sample of historical_data.csv for GitHub upload
This creates a 25MB sample that can be uploaded via web interface
"""

import pandas as pd
import os

print("=" * 60)
print("Creating Sample Data File")
print("=" * 60)

# Check file size
file_path = 'historical_data.csv'
file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
print(f"\nOriginal file size: {file_size_mb:.2f} MB")

# Read the file
print("\nReading historical_data.csv...")
df = pd.read_csv(file_path)
print(f"Total rows: {len(df):,}")

# Calculate sample size to get under 25MB
# Estimate: each row is approximately file_size / total_rows
bytes_per_row = os.path.getsize(file_path) / len(df)
target_size_bytes = 24 * 1024 * 1024  # 24MB to be safe
sample_size = int(target_size_bytes / bytes_per_row)

print(f"\nCreating sample with ~{sample_size:,} rows (target: <25MB)...")

# Create sample (random sample to maintain diversity)
df_sample = df.sample(n=min(sample_size, len(df)), random_state=42)

# Save sample
output_file = 'historical_data_sample.csv'
df_sample.to_csv(output_file, index=False)

# Check new file size
new_size_mb = os.path.getsize(output_file) / (1024 * 1024)
print(f"\nSample file created: {output_file}")
print(f"Sample file size: {new_size_mb:.2f} MB")
print(f"Rows in sample: {len(df_sample):,}")

print("\n" + "=" * 60)
print("SUCCESS! You can now upload 'historical_data_sample.csv'")
print("=" * 60)
print("\nNote: Update app.py to use 'historical_data_sample.csv' instead of 'historical_data.csv'")
print("Or keep both and let the app try sample first, then fall back to full file.")

