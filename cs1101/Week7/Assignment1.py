# Function to invert the student-course dictionary
def invert_student_course_dict(student_dict):
    # Create an empty dictionary for the inverted data
    inverted_dict = {}

    # Iterate through the original dictionary
    for student, courses in student_dict.items():
        # For each course the student is enrolled in
        for course in courses:
            # Check if the course is already a key in the inverted dictionary
            if course not in inverted_dict:
                inverted_dict[course] = []  # Initialize a list for that course
            # Append the student to the list of students for the course
            inverted_dict[course].append(student)
    
    return inverted_dict

# Sample input dictionary
student_course_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Invert the dictionary
inverted_dict = invert_student_course_dict(student_course_dict)

# Print original and inverted dictionaries
print("Original dictionary:")
print(student_course_dict)
# Output
# Original dictionary:
# {'Stud1': ['CS1101', 'CS2402', 'CS2001'], 'Stud2': ['CS2402', 'CS2001', 'CS1102']}
print("\nInverted dictionary:")
print(inverted_dict)
# Output
# Inverted dictionary:
# {'CS1101': ['Stud1'], 'CS2402': ['Stud1', 'Stud2'], 'CS2001': ['Stud1', 'Stud2'], 'CS1102': ['Stud2']}