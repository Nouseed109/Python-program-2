def calculate_grade(marks):
    if marks >= 90:
        return "A", "Outstanding! Keep up the excellent work!"
    elif marks >= 80:
        return "B", "Well done! You're doing great!"
    elif marks >= 70:
        return "C", "Good job! Keep pushing yourself!"
    elif marks >= 60:
        return "D", "Fair effort! You can do better!"
    else:
        return "F", "Don't worry! You've got this next time!"
def main():
    print("Simple Student Grade Calculator")
    print("-------------------------------")
    
    while True:
        try:
            marks = float(input("Enter your marks (0-100): "))
            if 0 <= marks <= 100:
                grade, message = calculate_grade(marks)
                print(f"\nGrade: {grade}")
                print(f"{message}")
                break
            else:
                print("Invalid marks. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
