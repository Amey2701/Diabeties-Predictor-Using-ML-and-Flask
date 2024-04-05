from flask import Flask, request, render_template  # Import necessary modules from Flask
import os  # Import os module for file handling
import pickle  # Import pickle module for loading the model

app = Flask(__name__)  # Create a Flask application instance

@app.route("/", methods=["GET", "POST"])  # Define a route for the root URL ("/") with GET and POST methods
def home():
    if request.method == "POST":  # Check if the request method is POST
        fn = "re.pkl"  # File name of the saved model

        if os.path.exists(fn):  # Check if the model file exists
            with open(fn, "rb") as f:  # Open the model file in binary mode for reading
                model = pickle.load(f)  # Load the model from the file

            # Get the values of "area" and "bedrooms" from the form data
            area = float(request.form["area"])
            bedrooms = float(request.form["bedrooms"])

            # Predict the price using the loaded model
            price = model.predict([[area, bedrooms]])

            # Format the message to be displayed
            msg = "Price = " + str(round(price[0], 2)) + " crs"

            # Render the "home.html" template with the message
            return render_template("home.html", msg=msg)
        else:
            print(fn, "does not exist")  # Print an error message if the model file doesn't exist
    else:
        return render_template("home.html")  # Render the "home.html" template for GET requests

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)  # Run the Flask app in debug mode with automatic reloading
