import pandas as pd
import os

directory = r'C:\Users\osandal\Downloads\GRI\data set 9'

# get a list of all the CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# create an Excel file
with pd.ExcelWriter('C:\\Users\\osandal\\Downloads\\GRI\\data set 9\\combined_dataset_1.xlsx') as writer:
    # loop through each CSV file and convert it to a separate sheet in the Excel file
    for csv_file in csv_files:
        csv_path = os.path.join(directory, csv_file)
        sheet_name = os.path.splitext(csv_file)[0]
        df = pd.read_csv(csv_path)

        # Convert time column to datetime object and format it
        #df['Date & Time'] = pd.to_datetime(df['Date & Time']).dt.strftime('%m/%d/%y %I:%M %p')

        df.to_excel(writer, sheet_name, index=False)