import os
import pandas as pd

directory = r'C:\Users\osandal\Downloads\AI\AI-GRI-main\GRI-Curing-temp\data set 9'  # Use raw string or double backslashes

csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

for file_name in csv_files:
    file_path = os.path.join(directory, file_name)
    df = pd.read_csv(file_path)
    
    # Assuming the time column is named 'time_column', you can change its format and rename it like this:
    df['Date & Time'] = pd.to_datetime(df['Date & Time'], format='%Y-%m-%d %H:%M:%S.%f').dt.strftime('%d/%m/%Y %H:%M:%S')
    
    # Drop the original 'time_column'
    #df.drop('Date & Time', axis=1, inplace=True)
    
    # Save the modified dataframe back to the same CSV file
    modified_file_path = os.path.join(directory, file_name)
    df.to_csv(modified_file_path, index=False)

    print(f"Modified {file_name} and saved successfully.")
