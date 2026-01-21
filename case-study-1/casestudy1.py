import json
import csv
import os
from abc import ABC, abstractmethod


# --- 1. Descriptors for Validation ---
class MarksValidator:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if not all(0 <= m <= 100 for m in value):
            print("Invalid Marks")
            raise ValueError("Error: Marks should be between 0 and 100")
        instance._marks = value


# --- 2. Decorators ---
def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result

    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        # Simulated privilege check
        role = "Admin"
        if role != "Admin":
            print("Access Denied: Admin privileges required")
            return None
        return func(*args, **kwargs)

    return wrapper


# --- 3. Classes & Inheritance ---
class Person(ABC):
    def __init__(self, p_id, name, dept):
        self.id = p_id
        self.name = name
        self.department = dept

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        # Destructor action
        pass


class Student(Person):
    marks = MarksValidator()  # Using Descriptor

    def __init__(self, s_id, name, dept, semester, marks):
        super().__init__(s_id, name, dept)
        self.semester = semester
        self.marks = marks

    @log_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = 'A' if avg >= 85 else 'B' if avg >= 70 else 'C'
        return avg, grade

    def get_details(self):
        return f"Name      : {self.name}\nRole      : Student\nDepartment: {self.department}"

    # Operator Overloading: Compare student performance
    def __gt__(self, other):
        avg_self = sum(self.marks) / len(self.marks)
        avg_other = sum(other.marks) / len(other.marks)
        return avg_self > avg_other


class Faculty(Person):
    def __init__(self, f_id, name, dept, salary):
        super().__init__(f_id, name, dept)
        self.__salary = salary  # Private attribute

    def get_details(self):
        return f"Name      : {self.name}\nRole      : Faculty\nDepartment: {self.department}"

    @property
    def salary(self):
        # Control access via property (Demonstrating control)
        return "Access Denied: Salary is confidential"


class Course:
    def __init__(self, code, name, credits, faculty_name):
        self.code = code
        self.name = name
        self.credits = int(credits)
        self.faculty_name = faculty_name

    # Operator Overloading: Merge credits
    def __add__(self, other):
        return self.credits + other.credits


# --- 4. Iterators & Generators ---
def student_record_generator(students_dict):
    print("Fetching Student Records...")
    for s_id, obj in students_dict.items():
        yield f"{s_id} - {obj.name}"


# --- 5. Main Management System ---
class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.faculties = {}
        self.courses = {}

    def add_student(self):
        try:
            sid = input("Student ID: ")
            if sid in self.students: raise Exception("Error: Student ID already exists")
            name = input("Student Name: ")
            dept = input("Department: ")
            sem = input("Semester: ")
            marks = list(map(int, input("Marks (5 subjects separated by space): ").split()))

            new_s = Student(sid, name, dept, sem, marks)
            self.students[sid] = new_s
            print("\nStudent Created Successfully")
            print("-" * 32)
            print(f"ID        : {sid}\nName      : {name}\nDepartment: {dept}\nSemester  : {sem}")
        except Exception as e:
            print(e)

    def add_faculty(self):
        fid = input("Faculty ID: ")
        name = input("Faculty Name: ")
        dept = input("Department: ")
        salary = input("Monthly Salary: ")
        self.faculties[fid] = Faculty(fid, name, dept, salary)
        print("\nFaculty Created Successfully")
        print("-" * 32)
        print(f"ID        : {fid}\nName      : {name}\nDepartment: {dept}")

    def add_course(self):
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = input("Credits: ")
        fid = input("Faculty ID: ")
        if fid in self.faculties:
            f_name = self.faculties[fid].name
            self.courses[code] = Course(code, name, credits, f_name)
            print("\nCourse Added Successfully")
            print("-" * 32)
            print(f"Course Code : {code}\nCourse Name : {name}\nCredits     : {credits}\nFaculty     : {f_name}")
        else:
            print("Error: Faculty ID not found.")

    def enroll_student(self):
        sid = input("Student ID: ")
        code = input("Course Code: ")
        if sid in self.students and code in self.courses:
            print("\nEnrollment Successful")
            print("-" * 32)
            print(f"Student Name : {self.students[sid].name}\nCourse       : {self.courses[code].name}")
        else:
            print("Error: Invalid Student or Course ID.")

    def calculate_perf(self):
        sid = input("Student ID: ")
        if sid in self.students:
            s = self.students[sid]
            avg, grade = s.calculate_performance()
            print("\nStudent Performance Report")
            print("-" * 32)
            print(f"Student Name : {s.name}\nMarks        : {s.marks}\nAverage      : {avg}\nGrade        : {grade}")
        else:
            print("Error: Student not found.")

    def compare_students(self):
        s1_id = input("Enter first Student ID: ")
        s2_id = input("Enter second Student ID: ")
        if s1_id in self.students and s2_id in self.students:
            s1, s2 = self.students[s1_id], self.students[s2_id]
            print("\nComparing Students Performance")
            print("-" * 32)
            print(f"{s1.name} > {s2.name} : {s1 > s2}")

    def generate_reports(self):
        # CSV Report
        with open('students_report.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Department', 'Average', 'Grade'])
            for s in self.students.values():
                avg, grade = s.calculate_performance()
                writer.writerow([s.id, s.name, s.department, avg, grade])

        # JSON Save
        data = [{"id": s.id, "name": s.name, "department": s.department, "semester": s.semester, "marks": s.marks}
                for s in self.students.values()]
        with open('students.json', 'w') as f:
            json.dump(data, f, indent=2)

        print("CSV Report (students_report.csv) generated.")
        print("Student data successfully saved to students.json")

    def run(self):
        while True:
            print("\n--- University Menu ---")
            print(
                "1. Add Student\n2. Add Faculty\n3. Add Course\n4. Enroll Student\n5. Calculate Performance\n6. Compare Students\n7. Generate Reports\n8. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_faculty()
            elif choice == '3':
                self.add_course()
            elif choice == '4':
                self.enroll_student()
            elif choice == '5':
                self.calculate_perf()
            elif choice == '6':
                self.compare_students()
            elif choice == '7':
                self.generate_reports()
            elif choice == '8':
                print("Thank you for using Smart University Management System")
                break
            else:
                print("Invalid Choice.")


if __name__ == "__main__":
    system = UniversitySystem()
    system.run()