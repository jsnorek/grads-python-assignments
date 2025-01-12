import os # For interacting with the file system
from flask import Flask, request, jsonify, render_template # For Flask
from flask_cors import CORS # Allows handling Cross-Origin Resource Sharing (CORS) which is necessary for making secure API requests from different origins.
from utils import process_file, upload_to_web_service # Import functions 

app = Flask(__name__) # Initializes Flask application
CORS(app) # Configures the Flask application to handle CORS

# Defines route for home page
@app.route('/')
# Function to handle requests to the home page
def home():
    feedback_dir = 'data/feedback' # Specifies the directory where feedback files are located
    feedbacks = [] # Initializes empty list to store feedback data

    if os.path.isdir(feedback_dir): # Checks if the feedback directory exists
        # Lists all .txt files in the feedback directory
        files = [f for f in os.listdir(feedback_dir) if f.endswith('.txt')]

        for file in files: # Iterates through each feedback file
            file_path = os.path.join(feedback_dir, file) # Constructs the path for each feedback file
            feedback_dict = process_file(file_path) # Processes the file to extract feedback data
            if feedback_dict: # Checks if feedback data was successfully extracted
                feedbacks.append({'file': file, 'feedback': feedback_dict}) # Appends feedback data to the list
    # Renders the index.html template with the feedback data
    return render_template('index.html', feedbacks=feedbacks)

# Defines a route for displayihng individual feedback files
@app.route('/feedback/<filename>')
# Function to handle requests to this route
def show_feedback(filename): 
    feedback_dir = 'data/feedback' # Specifies the directory where feedback files are stored
    file_path = os.path.join(feedback_dir, filename) # Creates the file path for the feedback files
    feedback_dict = process_file(file_path) # Processes the file to extract feedback data
    # Renders the feedback.html template with the feedback data
    return render_template('feedback.html', feedback=feedback_dict, file=filename)

# Defines a POST route to receive feedback
@app.route('/feedback', methods=['POST'])
# Function to handle POST requests to this route
def receive_feedback(): 
    """
    Endpoint to receive POST request data from client script.
    """
    data = request.get_json() # Extracts JSON data from the POST request body
    if data: # Checks if data was received
        print(f"Received feedback: {data}") # Prints the received feedback data
        # Returns a success message and HTTP status 200
        return jsonify({"message": "Feedback received successfully."}), 200
    else:
        # Returns an error message and HTTP status 400
        return jsonify({"message": "No data received."}), 400

if __name__ == '__main__': # Ensures script is running directly
    app.run(host='0.0.0.0', port=8000, debug=True) # Runs flask application on port 8000


