import mysql.connector


def connect():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="school"
    )


def create_student(name, age):
    connection = connect()
    cursor = connection.cursor()
    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(sql, values)
    connection.commit()
    print(f"Student {name} added successfully!")
    cursor.close()
    connection.close()


def read_students():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    if result:
        for student in result:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")
    else:
        print("No students found.")
    cursor.close()
    connection.close()


def update_student(student_id, name=None, age=None):
    connection = connect()
    cursor = connection.cursor()
    if name and age:
        sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
        values = (name, age, student_id)
    elif name:
        sql = "UPDATE students SET name = %s WHERE id = %s"
        values = (name, student_id)
    elif age:
        sql = "UPDATE students SET age = %s WHERE id = %s"
        values = (age, student_id)
    cursor.execute(sql, values)
    connection.commit()
    print(f"Student ID {student_id} updated successfully!")
    cursor.close()
    connection.close()


def delete_student(student_id):
    connection = connect()
    cursor = connection.cursor()
    sql = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    cursor.execute(sql, values)
    connection.commit()
    print(f"Student ID {student_id} deleted successfully!")
    cursor.close()
    connection.close()


create_student("Alice", 20)
create_student("Bob", 22)


print("\nList of students:")
read_students()


update_student(1, name="Alicia", age=21)


print("\nList of students after update:")
read_students()


delete_student(2)

print("\nList of students after deletion:")
read_students()


# Output
# Student Alice added successfully!
# Student Bob added successfully!

# List of students:
# ID: 1, Name: Alice, Age: 20
# ID: 2, Name: Bob, Age: 22

# Student ID 1 updated successfully!

# List of students after update:
# ID: 1, Name: Alicia, Age: 21
# ID: 2, Name: Bob, Age: 22

# Student ID 2 deleted successfully!

# List of students after deletion:
# ID: 1, Name: Alicia, Age: 21
