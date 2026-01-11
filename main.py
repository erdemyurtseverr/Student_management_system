import sqlite3
conn=sqlite3.connect("Basic_data.db")
cursor=conn.cursor()
#We handle the basic import and sql commands.

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)
""")
#this table stores student datas.

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
course_name TEXT,
course_id INTEGER PRIMARY KEY AUTOINCREMENT
)
""")
#this table stores student's course datas.

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (

id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER,
course_id INTEGER,
grade INTEGER NOT NULL DEFAULT 0 CHECK(grade BETWEEN 0 AND 100),
UNIQUE (student_id, course_id),

FOREIGN KEY (student_id) REFERENCES students(id),
FOREIGN KEY (course_id) REFERENCES courses(course_id)


     
)           
""")
#This table stores the grades that students receive for each course.

def connect_to_db():
    conn=sqlite3.connect("Basic_data.db")
    cursor=conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    return conn,cursor

def add_students_to_db(student_names):
    conn,cursor=connect_to_db()
    dt=((name,) for name in student_names)
    cursor.executemany("INSERT INTO students (name) VALUES(?)",
                       dt)
    #Executemany tuple değerler içeren bir liste ekler aslında
    #(name,) ile string değeri tuple haline getirdik
    #(ali)=string , (ali,)=tuple
    conn.commit()
    cursor.close()
    conn.close()

def add_courses_to_db(course_names):
    conn,cursor=connect_to_db()
    dt=((name,) for name in course_names)
    cursor.executemany("INSERT INTO courses (course_name) VALUES(?)",
                       dt)
    conn.commit()
    cursor.close()
    conn.close()

def add_grades_to_db(grades):
    conn,cursor=connect_to_db()
    cursor.executemany("INSERT INTO grades (student_id, course_id, grade) VALUES(?,?,?)",
                       grades)
    conn.commit()
    cursor.close()
    conn.close()


def get_student_id_by_name(name):
    conn, cursor = connect_to_db()
    cursor.execute(
        "SELECT id FROM students WHERE name = ?",
        (name,)
    )
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


def get_course_id_by_name(course_name):
    conn, cursor = connect_to_db()
    cursor.execute(
        "SELECT course_id FROM courses WHERE course_name = ?",
        (course_name,)
    )
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def menu():
    while True:
        try:
            print("------------------------------")
            print("1. Add students")
            print("2. Add courses")
            print("3. Add grades")
            print("4. Quit")
            print("------------------------------")
            option=int(input("Enter your choice: "))
            if option==1:
                add_students_to_db(input("Enter student names(comma separated) : ").split(","))
            elif option==2:
                add_courses_to_db(input("Enter course names(comma separated) : ").split(","))
            elif option == 3:
                student_name = input("Enter student name: ").strip()
                course_name = input("Enter course name: ").strip()

                try:
                    grade = int(input("Enter grade (0-100): "))
                except ValueError:
                    print("Grade must be a number.")
                    continue

                if not 0 <= grade <= 100:
                    print("Grade must be between 0 and 100.")
                    continue

                student_id = get_student_id_by_name(student_name)
                if student_id is None:
                    print("Student not found.")
                    continue

                course_id = get_course_id_by_name(course_name)
                if course_id is None:
                    print("Course not found.")
                    continue

                try:
                    add_grades_to_db([(student_id, course_id, grade)])
                    print("Grade added successfully.")
                except sqlite3.IntegrityError:
                    print("This student already has a grade for this course.")

            elif option==4:
                print("Thank you for using this program")
                break
            else:
                print("Invalid option.\nPlease try again.")
        except ValueError:
            print("Please enter a valid choice.")
menu()

