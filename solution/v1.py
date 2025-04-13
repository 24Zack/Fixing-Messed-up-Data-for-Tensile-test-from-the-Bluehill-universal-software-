import pandas as pd

# Load the CSV file - change the filename with the correct path if needed
# Ensure the file is in the same directory or provide the full path
# to the file.
# The file is expected to be in the format: Time;Displacement;Force
# The first row is a header, and the second row contains units.
# The third row and onwards contain the data.
# The delimiter is ';' and the decimal separator is ','.
input_filename = "Tensile_test_PE.csv"
try:
    df = pd.read_csv(input_filename, delimiter=';', decimal=',', skiprows=[1])
    print(f"File {input_filename} loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file {input_filename} was not found.")
    exit(1)

# Check if the necessary columns are present
required_columns = ["Time", "Displacement", "Force"]
if not all(column in df.columns for column in required_columns):
    print(f"Error: The input file must contain the columns: {required_columns}")
    exit(1)

# Check if the DataFrame has at least 3 rows
if len(df) < 3:
    print("Error: The input file must contain at least 3 rows.")
    exit(1)

print("Initial DataFrame:")
print(df)

# Clean the "Displacement" column
df["Displacement"] = df["Displacement"].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
df["Displacement"] = df["Displacement"].str.replace(r'[^0-9.]', '', regex=True)

# Remove extra periods
df["Displacement"] = df["Displacement"].apply(lambda x: x if x.count('.') <= 1 else x.replace('.', '', x.count('.') - 1))

# Convert to float
df["Displacement"] = df["Displacement"].astype(float)

# Loop through each row in the DataFrame
for i in range(1, len(df) - 1):
    current_disp = df.loc[i, "Displacement"]
    prev_disp = df.loc[i - 1, "Displacement"]
    next_disp = df.loc[i + 1, "Displacement"]
    
    # Check if the current displacement is less than both its neighbors
    if current_disp < prev_disp and current_disp < next_disp:
        df.loc[i, "Displacement"] = current_disp * 10

print("Modified DataFrame:")
print(df)

# Save the modified DataFrame to a new CSV file
output_filename = "Tensile_test_modified_PE.csv"
df.to_csv(output_filename, index=False)

print(f"Modified file saved as {output_filename}")