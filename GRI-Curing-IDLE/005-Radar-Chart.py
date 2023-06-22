import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file and select the desired columns
data = pd.read_excel(r'C:\Users\osandal\OneDrive - Global Rubber Industries (Pvt) Ltd\Desktop\Github\AI-GRI\GRI-Curing-IDLE\data set 9\combined_dataset.xlsx')
selected_columns = data.iloc[:, 2:7]  # Select columns B to F (index 2 to 6)

# Calculate the mean values for each column
column_means = selected_columns.mean()

# Create a list of column names
column_names = selected_columns.columns

# Plot the radar chart
plt.figure(figsize=(8, 6))
plt.polar(range(len(column_names)), column_means, marker='o')
plt.fill(range(len(column_names)), column_means, alpha=0.25)
plt.xticks(range(len(column_names)), column_names)
plt.title('Radar Chart')
plt.show()