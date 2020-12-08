'''
Austin Sickels
12/6/20
'''

import os.path

class Student:

    def __init__(self, name, time_week):
        self.username = name
        self.total_time_per_week = time_week

    def write_to_file(self, filename):
        filename.write(f"{self.username}\n")
        filename.write(f"{self.total_time_per_week}\n")


class Course:

    def __init__(self, name, input_credits, difficulty, confidence):
        self.course_name = name
        self.course_credits = input_credits
        self.course_difficulty = difficulty
        self.confidence = confidence

        # Optional variables default to None

        self.professor_name = None
        self.professor_difficulty = None
        self.grading_scale = None

    def set_optional_var(self, professor, difficulty, scale):
        self.professor_name = professor
        self.professor_difficulty = difficulty
        self.grading_scale = scale

    def write_to_file(self, filename):
        filename.write(f"{self.course_name}\n")
        filename.write(f"{self.course_credits}\n")
        filename.write(f"{self.course_difficulty}\n")
        filename.write(f"{self.confidence}\n")
        if self.professor_name is not None:
            filename.write(f"{self.professor_name}\n")
            filename.write(f"{self.professor_difficulty}\n")
            filename.write(f"{self.grading_scale}\n")



class Semester:

    def __init__(self, name, input_student, list_of_courses):
        self.semester_name = name
        self.student = input_student
        self.course_list = list_of_courses

    def print_semester(self):
        print(f"Semester: {self.semester_name}")
        print(f"Student: {self.student.username}")
        print("Courses", end=": ")
        for course in self.course_list:
            print(course.course_name, end=" ")
        print()

    def write_to_file(self, filename):
        filename.write(f"{self.semester_name}\n")
        filename.write(f"{self.student}\n")
        filename.wrote(f"{self.course_list}\n")


class ExamProject:

    def __init__(self, pe_name, c_name, date, time):
        self.name = pe_name
        self.class_name = c_name
        self.due_date = date
        self.time_to_complete = time

    def write_to_file(self, filename):
        filename.write(f"{self.name}\n")
        filename.write(f"{self.class_name}\n")
        filename.write(f"{self.due_date}\n")
        filename.write(f"{self.time_to_complete}\n")


def read_user_input():
    student_name = input("Enter your name: ")
    student_hours = input(
        "Enter the hours you can study per week, excluding class time: ")
    semester_name = input("Enter semester and year: ")
    me = Student(student_name, student_hours)
    course_list = []
    while True:
        course_name = input("Enter course name: ")
        course_credits = input("Enter number of credit hours: ")
        course_difficulty = input(
            "Enter projected course difficulty (1-100): ")
        course_confidence = input("How well do you know the material? (1-100): ")
        course = Course(course_name, course_credits, course_difficulty,
                        course_confidence)
        course_list.append(course)
        more_info = input(
            "Would you like to add more info for a better calculation? (y/n): ")
        if more_info == "y":
            professor_name = input("Enter professor\'s name: ")
            professor_difficulty = input("Enter professors\'s difficulty (1-5): ")
            passing_grade = input("Enter minimum grade for C-: ")
            course.set_optional_var(professor_name, professor_difficulty,
                                    passing_grade)
        exit_condition = input("Add another course? (y/n): ")
        if exit_condition == "n":
            break
    semester = Semester(semester_name, me, course_list)
    return semester

def read_file_input(filename):
    filename.readline()

def file_io():
    file = open("semester_info.txt", "r+")
    fileIn = file.readline()
    if fileIn == "BEGIN\n":
        read_file_input(file)
    else:
        output = read_user_input()
        file.write("BEGIN\n")
        file.write("STUDENT\n")
        output.student.write_to_file(file)
        file.write("ENDSTUDENT\n")
        file.write("SCHEDULE\n")
        for course in output.course_list:
            file.write("COURSE\n")
            course.write_to_file(file)
            file.write("ENDCOURSE\n")
        file.write("ENDSCHEDULE\n")
        #TODO the projects/exams section
        file.write("END")
    file.close()


if __name__ == '__main__':
    if not os.path.exists("semester_info.txt"):
        file_to_create = open("semester_info.txt", "w")
        file_to_create.close()
    file_io()