import os
import pandas as pd

# Set the directory containing the input Excel files
input_dir = r"H:\\GRI\\MIXING\\ST03"

# Set the directory where the output Excel file will be saved
output_dir = r"H:\\GRI\\MIXING\\ST03"

# Get a list of all Excel files in the input directory
excel_files = [file for file in os.listdir(input_dir) if file.endswith('.xlsx')]

# Create a new Excel file
writer = pd.ExcelWriter(os.path.join(output_dir, 'combined.xlsx'), engine='xlsxwriter')

# Loop through the input Excel files and add each file as a separate sheet to the new Excel file
for file in excel_files:
    # Set the sheet name to the original file name
    sheet_name = os.path.splitext(file)[0]
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(os.path.join(input_dir, file))
    # Write the DataFrame to a new sheet in the output Excel file
    df.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the output Excel file
writer.save()
