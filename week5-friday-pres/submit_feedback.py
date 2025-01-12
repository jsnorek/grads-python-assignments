# This page reads feedback files and uploads their contentst to the Flask web service using POST requests.
# It simulates a client sending data to the web service

import os
import requests

def process_file(file_path):
    """
    Process the content of a text file and return a dictionary with relevant information.
    Should extract: title, name, date, feedback.
    """
    feedback_dict = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 4:
                feedback_dict['title'] = lines[0].strip()
                feedback_dict['name'] = lines[1].strip()
                feedback_dict['date'] = lines[2].strip()
                feedback_dict['feedback'] = lines[3].strip()
            else:
                print(f"The file {file_path} does not contain enough lines.")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

    return feedback_dict

def upload_to_web_service(data):
    """
    Send a POST request to the web service with the data.
    """
    url = "http://localhost:8000/feedback"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"Successfully uploaded data: {data}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to upload data: {e}")
        return False

def main():
    feedback_dir = 'data/feedback'
    if not os.path.isdir(feedback_dir):
        print(f"Invalid directory: {feedback_dir}")
        return

    files = [f for f in os.listdir(feedback_dir) if f.endswith('.txt')]
    if not files:
        print("No files to process")
        return
    
    for file in files:
        file_path = os.path.join(feedback_dir, file)
        feedback_dict = process_file(file_path)
        if feedback_dict:
            success = upload_to_web_service(feedback_dict)
            if success:
                print(f"Uploaded feedback from {file}")
            else:
                print(f"Failed to upload feedback from {file}")
        else:
            print(f"Failed to process {file}")

    print("Processing complete.")

if __name__ == '__main__':
    main()
