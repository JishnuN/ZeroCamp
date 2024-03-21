import sqlite3

def create_tables():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students(first_name TEXT NOT NULL,last_name TEXT NOT NULL, student_id INTEGER NOT NULL PRIMARY KEY)")

    cursor.execute("CREATE TABLE IF NOT EXISTS subjects(name TEXT NOT NULL UNIQUE, subject_id INTEGER UNIQUE NOT NULL PRIMARY KEY)")

    cursor.execute("""CREATE TABLE IF NOT EXISTS results(
                   student_id INTEGER NOT NULL,
                   subject_id INTEGER NOT NULL,
                   marks INTEGER NOT NULL,
                   FOREIGN KEY (student_id) REFERENCES students(student_id),
                   FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) )""")
    con.commit()
    con.close()

##---------------------------------------------------------------

def add_student(first_name,last_name,student_id):
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.execute("INSERT INTO students VALUES(?,?,?)",(first_name,last_name,student_id))
    con.commit()
    con.close()

def add_sample_students():
    sample_list = [('Henry','Garcia','1'),('Grace','Smith','2'),('Eve','Johnson','3'),('Grace','Rodriguez','4'),('Alice','Smith','5'),('Charlie','Miller','6')]
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.executemany("INSERT INTO students VALUES (?,?,?)",sample_list)
    print(cursor.fetchall())
    con.commit()
    con.close()

def edit_by_id():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    id = input('enter student id: ')
    id = int(id)
    cursor.execute("SELECT * FROM students WHERE student_id = (?)",id)
    print(cursor.fetchall())
    first_name =input('enter first name: ')
    last_name = input('enter last name: ')
    cursor.execute("UPDATE students SET first_name = (?),last_name = (?) WHERE student_id = (?)",(first_name,last_name,id))
    print('\nstudent details updated.')
    con.commit()
    con.close()

def add_subjects():
    sub = [('Mathematics','1'),('Physics','2'),('Chemistry','3'),('Social Science','4'),('IT','5'),('Biology','6')]
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.executemany("INSERT INTO subjects VALUES (?,?)",sub)
    print(cursor.fetchall())
    con.commit()
    con.close()

def view_all():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM students""")
    print(cursor.fetchall())
    con.commit()
    con.close()

def view_marks():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    id = input("enter student id: ")
    cursor.execute("""SELECT students.first_name,students.last_name,subjects.name,results.marks FROM students LEFT JOIN results ON students.student_id=results.student_id LEFT JOIN subjects ON results.subject_id=subjects.subject_id WHERE students.student_id = (?)""",id)
    print(cursor.fetchall())
    con.commit()
    con.close()

def add_marks():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    student_id = input("enter student id: ")
    subject_id = input("enter subject id: ")
    mark = input("enter mark: ")
    cursor.execute("INSERT INTO results VALUES(?,?,?)",(student_id,subject_id,mark))
    cursor.execute("SELECT * FROM results WHERE student_id = (?)",student_id)
    con.commit()
    con.close()

def view_topper():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    subject = input('enter a subject id: ')
    cursor.execute("""SELECT students.first_name, students.last_name, results.marks 
                      FROM students 
                      JOIN results ON students.student_id=results.student_id WHERE results.subject_id = (?) ORDER BY marks DESC""",subject)
    print(cursor.fetchall())
    con.commit()
    con.close()
    
def avg_marks():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    subject = input("enter subject id: ")
    cursor.execute("SELECT avg(marks) FROM results WHERE subject_id = (?)",subject)
    print(cursor.fetchall())
    con.commit()
    con.close()

def top_5():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM results ORDER BY marks DESC LIMIT 5")
    print(cursor.fetchall())
    con.commit()
    con.close()

def view_subjects():
    con = sqlite3.connect('smsdb')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM subjects WHERE subject_id = 1")
    print(cursor.fetchall())
    con.commit()
    con.close()

def menu():
    def options():
        print("Student Management System")
        print("1. Add Student")
        print("2. Edit Student Name")
        print("3. Add Marks")
        print("4. View all Student Details")
        print("5. View marks of a student")
        print("6. View toppers of a subject")
        print("7. View average marks of a subject")
        print("8. View top 5 marks")
        print("q. Quit")
        return input("Enter your choice: ")

    while True:
        choice = options()
        try:
            choice = int(choice)
        except:
            choice = 'q'
        if choice == 'q':
          break
        if choice == 1:
            first_name = input("enter student  first name: ")
            last_name = input("enter student last name: ")
            student_id = input('enter stundent id: ')
            add_student(first_name,last_name,student_id)
        if choice == 2:
            edit_by_id()
        if choice == 3:
            add_marks()
        if choice == 4:
            view_all()
        if choice == 5:
            view_marks()
        if choice == 6:
            view_topper()
        if choice == 7:
            avg_marks()
        if choice == 8:
            top_5()

#------------------------------------------------------------------
create_tables()
#add_sample_students()
#add_subjects()
menu()   
            
      
 