import numpy as np
import matplotlib.pyplot as plt

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
values = [4, 3, 5, 2, 4]  # Values for each category

# Number of categories
num_categories = len(categories)

# Calculate angle for each category
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False)

# Create the radar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.5)  # Fill the area

# Set the labels for each category
ax.set_xticks(angles)
ax.set_xticklabels(categories)

# Set the y-axis limit
ax.set_ylim(0, 5)

# Set the title
ax.set_title('Radar Graph')

# Display the radar graph
plt.show()
