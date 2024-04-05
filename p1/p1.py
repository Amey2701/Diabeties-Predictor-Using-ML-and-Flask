import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the data from the CSV file into a pandas DataFrame
data = pd.read_csv("abp_march24.csv")
print(data)  # Print the loaded data (optional)

# Extract features (independent variables) and target (dependent variable) from the DataFrame
features = data[["area", "bedrooms"]]  # Features: "area" and "bedrooms"
target = data["price"]  # Target: "price"

# Initialize a Linear Regression model
model = LinearRegression()

# Train (fit) the model on the features and target
model.fit(features.values, target)

# Save the trained model to a file using pickle
with open("re.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Created")  # Print confirmation message
