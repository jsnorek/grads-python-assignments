import os # For interacting with the file system
import requests # For making HTTP requests
from flask import Flask, request, jsonify, render_template # For Flask
from flask_cors import CORS # Allows handling Cross-Origin Resource Sharing (CORS) which is necessary for making secure API requests from different origins.

app = Flask(__name__) # Initializes Flask application
CORS(app) # Configures the Flask application to handle CORS

# Function to process the file
def process_file(file_path):
    """
    Process the content of a text file and return a dictionary with relevant information.
    Extracts: title, name, date, feedback
    """
    feedback_dict = {} # Initializes empty dictionary to store feedback information
    try: # Try block to handle potential errors
        with open(file_path, 'r') as file: # Opens the file in read mode
            lines = file.readlines() # Reads all lines of the file into a list
            if len(lines) >= 4:  # Ensure there are at least 4 lines to extract required information
                feedback_dict['title'] = lines[0].strip() # Extracts and strips the first line as the title
                feedback_dict['name'] = lines[1].strip() # Extracts and strips the second line as the name
                feedback_dict['date'] = lines[2].strip() # Extracts and strips the third line as the date
                feedback_dict['feedback'] = lines[3].strip() # Extracts and strips the fourth line as feedback
            else:
                print(f"The file {file_path} does not contain enough lines.")
    except IOError as e: # Handles any I/O errors that occur while reading the file
        # Prints error message
        print(f"Error reading file {file_path}: {e}")

    return feedback_dict # Returns the dictionary with extracted feedback information

# Function to upload data to web service
def upload_to_web_service(data):
    """
    Send a POST request to the web service with the data.
    """
    url = "http://localhost:8000/feedback"
    try:
        # Sends POST request with JSON data to the url
        response = requests.post(url, json=data)
        # Raises an error if the request returned an unsuccessful status code
        response.raise_for_status()
        print(f"Successfully uploaded data: {data}")  # Prints success message
        return True # Returns True if data upload is successful
    # Handles exceptions raised during request
    except requests.exceptions.RequestException as e:
        print(f"Failed to upload data: {e}") # Prints error message if data upload fails
        return False # Returns False if data upload fails

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


