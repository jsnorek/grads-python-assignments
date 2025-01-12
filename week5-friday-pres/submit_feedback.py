# This page reads feedback files and uploads their contentst to the Flask web service using POST requests.
# It servers as the client-side component and simulates a client sending data to the web service

import os
from utils import process_file, upload_to_web_service
    
# Main function that checks the feedback directory, lists all feedback files, processes each file to extract information, uploads the data to a web service, and logs the results of each step
def main():
    feedback_dir = 'data/feedback' # Specifies the directory where feedback files are located
    if not os.path.isdir(feedback_dir): # Checks if feedback_dir is a valid directory
        print(f"Invalid directory: {feedback_dir}") # Prints error message if not valid
        return

    files = [f for f in os.listdir(feedback_dir) if f.endswith('.txt')] # Lists all .txt files in the feedback_dir
    if not files: # Checks if list of .txt files is empty
        print("No files to process")
        return
    
    for file in files: # Iterates through each .txt file in files list
        file_path = os.path.join(feedback_dir, file) # Creates full file path by joining directory path and file name
        feedback_dict = process_file(file_path) # Calls process_file function and passes full file path to it to get the dictionary with extracted feedback info
        if feedback_dict: # Checks if the returned dictionary is valid
            success = upload_to_web_service(feedback_dict) # If success, calls upload_to_web_service function and passes the feedback dictionary
            if success:
                print(f"Uploaded feedback from {file}")
            else:
                print(f"Failed to upload feedback from {file}")
        else:
            print(f"Failed to process {file}")

    print("Processing complete.")

if __name__ == '__main__':
    main()
