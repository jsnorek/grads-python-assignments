import pandas as pd

def read_csv(file_path):
    try:
        data = pd.read_csv(file_path) # Read the CSV file with pandas
        print("Data successfully read from CSV file:")
        print(data)
        return data
    except FileNotFoundError: # This is an error that occurs when the targeted file is not found
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError: # This exception raised in pd.read_csv when empty data or header is encountered.
        print(f"Error: The file {file_path} is empty.")
        return None
    except pd.errors.ParserError: # This exception raised is a generic error for errors encountered when functions like read_csv or read_html are parsing contents of a file.
        print(f"Error: There was a problem parsing the file {file_path}.")
        return None

# Function to calculate the average of the data defined from the CSV file
def calculate_average(data):
    # Creates list of subjects for the columns we want to pull from 
    subjects = ['Maths Grade', 'Science Grade', 'English Grade']
    # Initializes an empty dictionary to store the average grade for each subject with key value pairs - subject names as keys and their averages as values
    averages = {} 
    # For loop to iterate over each subject in the 'subjects' list
    for subject in subjects:
        # Calculates the mean for each subject and stores it in the 'averages' dictionary
        averages[subject] = data[subject].mean() 
    # Returns the 'averages' dictionary
    return averages 

# Function to find the student(s) with the highest overall grade
def find_highest_overall_grade(data):
    # This selects columns from our DataFrame, calculates the mean across the horizontal axis, and then adds a new column, 'Overall Grade' with the mean values
    data['Overall Grade'] = data[['Maths Grade', 'Science Grade', 'English Grade']].mean(axis=1) # axis=1 specifies the horizontal axis(rows), axis=0 specifies the vertical axis(columns)
    # Accesses 'Overall Grade' column, finds the max value, and assigns it to max_grade 
    max_grade = data['Overall Grade'].max() 
    # Filters data to where 'Overall Grade' equals max_grade, selects the now-filtered 'Name' column, and uses tolist() to list the name(s) of the student(s) with the highest overall grade
    top_students = data[data['Overall Grade'] == max_grade]['Name'].tolist() 
    # Returns top_students and max_grade
    return top_students, max_grade # When you return multiple values separated by commas in a return statement, Python automatically packs them into a tuple, example: : (["Alice", "Bob", "Charlie"], 95)

# Function to find the subject with the highest average score from the 'averages'
def subject_with_highest_average(averages):
    # Max() function finds key with highest value
    return max(averages, key=averages.get) # key=averages.get makes sure to compare the values and then .get retrieves the value for each key(subject)

# Function to generate the report using averages, top_students, max_grade, and top_subject
def generate_report(averages, top_students, max_grade, top_subject):
    # Initializes report string with a header and newline char \n
    report = "Average Grades:\n" 
    # For loop that iterates through each subject and average in the averages dictionary
    for subject, average in averages.items(): # .items() returns a view object of the key-value pairs
        # Appends each iteration string to the report
        report += f"{subject}: {average:.2f}\n" # {average:.2f} formats to two decimal places

    # Appends another header string to the report
    report += "\nTop Students(s):\n"
    # For loop that iterates through students in top_students list
    for student in top_students:
        # For each student, append string to the report
        report += f"{student} with an overall grade of {max_grade: 2f}\n" # {max_grade:.2f} formats to two decimal places
    
    # Appends another header string to the report
    report += "\nSubject with Highest Average Grade:\n"
    # Appends string with top_subject and its average grade to the report
    report += f"{top_subject} with an average grade of {averages[top_subject]:2f}\n" # {average[top_subject]:.2f} formats to two decimal places

    # Returns final report string
    return f"This is the report:\n {report}"

# Initializes variable with string for CSV file path
file_path = 'students_grades.csv'

# Error test for incorrect file name
# file_path = 'student_grades.csv'

# Test for accounting for NaN data entries in the CSV file
# file_path = 'science_grade.csv'

# Calls function read_csv() that reads CSV file and returns formatted data
data = read_csv(file_path)

# Checks if data variable is not None to make sure it was successfully read
if data is not None:
    # Convert grades from the specified columns to numeric values, handle errors by converting non-numeric values to NaN
    data[['Maths Grade', 'Science Grade', 'English Grade']] = data[['Maths Grade', 'Science Grade', 'English Grade']].apply(pd.to_numeric, errors='coerce') # .apply() method by default applies a function to the each column. pd.to_numeric function attempts to converts values to numeric type. errors='coerce' catches pd.to_numeric's errors and converts invalid parsing to NaN instead of thowing error
    
    # Calls function to calculate the averages with the data as an argument
    averages = calculate_average(data)

    # Calls function to find the highest overall grade and then identifies top_students and max_grade from the function
    top_students, max_grade = find_highest_overall_grade(data)

    # Another way to unpack top_students and max_grade
    # highest_results = find_highest_overall_grade(data)
    # top_students, max_grade = highest_results

    # Calls function to find the subject with the highest average using averages as an arugment
    top_subject = subject_with_highest_average(averages)

    # Calls function to generate the report using averages, top_students, max_grade, and top_subject as arguments
    report = generate_report(averages, top_students, max_grade, top_subject)
    # Prints the report to the console
    print(report)

    # Test for displaying the averages
    # formatted_averages = {subject: float(f"{average:.2f}") for subject, average in averages.items()}
   
    # print(f"This is the average for each subject: {formatted_averages}")