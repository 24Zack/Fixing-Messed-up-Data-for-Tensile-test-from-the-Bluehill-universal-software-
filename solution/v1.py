import pandas as pd

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


df["Displacement"] = df["Displacement"].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
df["Displacement"] = df["Displacement"].str.replace(r'[^0-9.]', '', regex=True)


df["Displacement"] = df["Displacement"].apply(lambda x: x if x.count('.') <= 1 else x.replace('.', '', x.count('.') - 1))

df["Displacement"] = df["Displacement"].astype(float)


for i in range(1, len(df) - 1):
    current_disp = df.loc[i, "Displacement"]
    prev_disp = df.loc[i - 1, "Displacement"]
    next_disp = df.loc[i + 1, "Displacement"]
    
    # Check if the current displacement is less than both its neighbors
    if current_disp < prev_disp and current_disp < next_disp:
        df.loc[i, "Displacement"] = current_disp * 10

print("Modified DataFrame:")
print(df)


output_filename = "Tensile_test_modified_PE.csv"
df.to_csv(output_filename, index=False)

print(f"Modified file saved as {output_filename}")
