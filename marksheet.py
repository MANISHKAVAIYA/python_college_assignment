# marksheet 
    def create_marksheet():
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")

    print("Enter marks in five subjects:")
    math = float(input("Math: "))
    science = float(input("Science: "))
    english = float(input("English: "))
    history = float(input("History: "))
    computer = float(input("Computer: "))

    total_marks = math + science + english + history + computer
    percentage = (total_marks / 500) * 100

    print("\nMark Sheet")
    print("==========")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print("Subjects: ")
    print("==========")
    print(f"Math: {math}")
    print(f"Science: {science}")
    print(f"English: {english}")
    print(f"History: {history}")
    print(f"Computer: {computer}")
    print("==========")
    print(f"Total Marks: {total_marks} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print("==========")

create_marksheet()
