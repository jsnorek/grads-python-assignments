# Contains common functions between main.py and submit_feedback.py to maintain code efficiency and reduce redundancy.
# Contains the process_file and upload_to_web_service functions used in both scripts (main.py, and submit_feedback.py)

import os
import requests

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