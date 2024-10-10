import pandas as pd

# Load the dataset from the CSV file 
def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    print("Column names:", data.columns)
    data.columns = data.columns.str.strip()  
    return data

# Display records 
def display_records(data):
    print(data.head())

# Selection sort
def selection_sort(data):
    n = len(data)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if data.iloc[j]['math_score'] > data.iloc[max_index]['math_score']:
                max_index = j
        data.iloc[i], data.iloc[max_index] = data.iloc[max_index], data.iloc[i]  

# Insertion sort
def insertion_sort(data):  
    for i in range(1, len(data)):
        key = data.iloc[i]
        j = i - 1
        while j >= 0 and data.iloc[j]['reading_score'] > key['reading_score']:
            j -= 1
        data.iloc[j + 1], data.iloc[i] = data.iloc[i], data.iloc[j + 1]

# Linear search for student ID
def linear_search(data, student_id):
    for index, row in data.iterrows():
        if row['Student ID'] == student_id:
            return row
    return None

# Binary search based on reading score 
def binary_search(data, score):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data.iloc[mid]['reading_score'] == score:
            return data.iloc[mid]
        elif data.iloc[mid]['reading_score'] < score:
            low = mid + 1
        else:
            high = mid - 1
    return None 

# Calculate average scores and passing percentage
def calculate_statistics(data):
    grades = data['grade'].unique()
    stats = {}
    for grade in grades:
        grade_data = data[data['grade'] == grade]
        avg_reading = grade_data['reading_score'].mean()
        avg_math = grade_data['math_score'].mean()
        passing_reading = (grade_data['reading_score'] >= 70).mean() * 100
        passing_math = (grade_data['math_score'] >= 70).mean() * 100 
        stats[grade] = {
            'Average Reading Score': avg_reading,
            'Average Math Score': avg_math,
            'Passing Percentage in Reading': passing_reading,
            'Passing Percentage in Math': passing_math
        }
    return stats

# Main function 
def main():
    file_path = 'students_complete.csv'
    data = load_data(file_path)
    display_records(data)

    # Sort and display top Math Scores
    selection_sort(data)
    print("\nTop records sorted by Math Score (descending):")
    print(data.head())   

    # Sort and display top Reading Scores 
    insertion_sort(data)
    print("\nTop records sorted by Reading Score (ascending):")
    print(data.head())

    # Search for student ID
    student_id = input("\nEnter a Student ID to find their scores: ")
    student_record = linear_search(data, student_id)
    if student_record is not None:
        print(f"Student Record:\n{student_record}")
    else:
        print("Student ID not found.")

    # Search for reading score 
    print("\nEnter a Reading Score to search for a student:")
    score = float(input())
    found_student = binary_search(data.sort_values('reading_score'), score)  
    if found_student is not None:
        print(f"Student Record with Reading Score {score}:\n{found_student}")
    else:
        print("No student found with that Reading Score.")

    # Calculate and print statistics 
    stats = calculate_statistics(data)
    print("\nAverage Scores and Passing Percentages by Grade:")
    for grade, stat in stats.items():
        print(f"Grade {grade}: {stat}")

if __name__ == "__main__":
    main()
