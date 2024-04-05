import pickle  # Import the pickle module for loading the model
import os  # Import the os module for file handling

fn = "re.pkl"  # File name of the saved model

# Check if the model file exists
if os.path.exists(fn):
    # Open the file in binary mode for reading
    with open(fn, "rb") as f:
        # Load the model from the file
        model = pickle.load(f)
    print("Model loaded")  # Print confirmation message
else:
    print(fn, "does not exist")  # Print error message if the model file doesn't exist

# Model usage
if 'model' in locals():  # Check if the model is successfully loaded
    # Get user input for area and number of bedrooms
    area = float(input("Enter area: "))
    bedrooms = float(input("Enter number of bedrooms: "))

    # Predict the price using the loaded model
    price = model.predict([[area, bedrooms]])

    # Print the predicted price
    print("Predicted price:", round(price[0], 2), "Crs")
else:
    print("Model is not loaded. Cannot make predictions.")  # Print error message if the model is not loaded
