import pandas as pd

# Create a dictionary with data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Amsterdam", "Rotterdam", "Utrecht"]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)