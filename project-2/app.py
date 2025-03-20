# Dictionary to store student names and their marks
student_marks = {}

# Function to add a new student
def add_student(name: str, grade: int):
    student_marks[name] = grade
    print(f"{name} added with marks {grade}.")

# Function to update an existing student's marks
def update_student(name: str, grade: int):
    if name in student_marks:
        student_marks[name] = grade
        print(f"Marks for {name} have been updated to {grade}!")
    else:
        print(f"{name} not found!")

# Function to delete a student from the records
def delete_student(name: str):
    if name in student_marks:
        del student_marks[name]
        print(f"{name} has been successfully deleted!")
    else:
        print(f"{name} not found!")

# Function to display all student records
def display_all_students():
    if student_marks:
        print("\nStudent Records:")
        for name, grade in student_marks.items():
            print(f"{name}: {grade}")
    else:
        print("No students available.")

# Main function to run the menu-driven program
def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter student name: ")
                grade = int(input("Enter student marks: "))
                add_student(name, grade)
            elif choice == 2:
                name = input("Enter student name: ")
                grade = int(input("Enter updated marks: "))
                update_student(name, grade)
            elif choice == 3:
                name = input("Enter student name: ")
                delete_student(name)
            elif choice == 4:
                display_all_students()
            elif choice == 5:
                print("Program closed.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Ensures the program runs only when executed directly
if __name__ == "__main__":
    main()
