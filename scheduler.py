'''
Austin Sickels
12/6/20
'''

import os.path


class Student:

    def __init__(self, name, time_week):
        self.username = name
        self.total_time_per_week = time_week

    def print_student(self):
        print(
            f"{self.username} plans to study {self.total_time_per_week} hours per week")

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

    def print_course(self):
        print(
            f"{self.course_name}: {self.course_credits} credits; {self.course_difficulty}/100 difficulty; {self.confidence}/100 confidence",
            end="")
        if self.professor_name is not None:
            print(
                f"; Professor {self.professor_name}; {self.professor_difficulty}/5 professor difficulty; {self.grading_scale}/100 minimum C-")

    def set_optional_var(self, professor, difficulty, scale):
        self.professor_name = professor
        self.professor_difficulty = difficulty
        self.grading_scale = scale

    def write_to_file(self, filename):
        filename.write(f"{self.course_name}\n")
        filename.write(f"{self.course_credits}\n")
        filename.write(f"{self.course_difficulty}\n")
        filename.write(f"{self.confidence}\n")
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
        course_confidence = input(
            "How well do you know the material? (1-100): ")
        course = Course(course_name, course_credits, course_difficulty,
                        course_confidence)
        course_list.append(course)
        more_info = input(
            "Would you like to add more info for a better calculation? (y/n): ")
        if more_info == "y":
            professor_name = input("Enter professor\'s name: ")
            professor_difficulty = input(
                "Enter professors\'s difficulty (1-5): ")
            passing_grade = input("Enter minimum grade for C-: ")
            course.set_optional_var(professor_name, professor_difficulty,
                                    passing_grade)
        exit_condition = input("Add another course? (y/n): ")
        if exit_condition == "n":
            break
    semester = Semester(semester_name, me, course_list)
    print("Data successfully saved")
    return semester


def read_file_input(filename):
    semester_name = filename.readline()
    fileIn = filename.readline().strip('\n')
    course_list = []
    while fileIn != "END":
        if fileIn == "STUDENT":
            given_student = Student(filename.readline().strip('\n'), filename.readline().strip('\n'))
        elif fileIn == "COURSE":
            given_course = Course(filename.readline().strip('\n'), filename.readline().strip('\n'),
                                  filename.readline().strip('\n'), filename.readline().strip('\n'))
            given_course.set_optional_var(filename.readline().strip('\n'),
                                          filename.readline().strip('\n'),
                                          filename.readline().strip('\n'))
            course_list.append(given_course)
        fileIn = filename.readline().strip('\n')
    semester = Semester(semester_name, given_student, course_list)
    return semester


def write_to_file(file):
    semester_input = read_user_input()
    file.write("BEGIN\n")
    file.write(f"{semester_input.semester_name}\n")
    file.write("STUDENT\n")
    semester_input.student.write_to_file(file)
    file.write("ENDSTUDENT\n")
    file.write("SCHEDULE\n")
    for course in semester_input.course_list:
        file.write("COURSE\n")
        course.write_to_file(file)
        file.write("ENDCOURSE\n")
    file.write("ENDSCHEDULE\n")
    # TODO the projects/exams section
    file.write("END")


def file_io():
    file = open("semester_info.txt", "r+")
    fileIn = file.readline()
    if fileIn == "BEGIN\n":
        semester = read_file_input(file)
        print(f'Hello, {semester.student.username}. '
              f'Select an option from the list below:')
        option_switch = input(f"a: Print this weeks schedule\n"
                              f"b: Print student information\nc: Print all "
                              f"courses\nd: Overwrite saved schedule\n"
                              f"e: Delete all "
                              f"information and exit\nq: Quit\n")
        while option_switch != "q":
            if option_switch == "a":
                print("Nothing yet!")
            elif option_switch == "b":
                semester.student.print_student()
            elif option_switch == "c":
                for course in semester.course_list:
                    course.print_course()
            elif option_switch == "d":
                confirmation = input(
                    "This will permanently overwrite all saved information, are you sure? (y/n)\n")
                if confirmation == "y":
                    print("Not working yet!")
                    # semester_input = read_user_input()
                    break
            elif option_switch == "e":
                confirmation = input(
                    "This will permanently remove all saved information, are you sure? (y/n)\n")
                if confirmation == "y":
                    os.remove("semester_info.txt")
                    break
            elif option_switch == "q":
                break
            option_switch = input()

    else:
        write_to_file(file)
    file.close()


if __name__ == '__main__':
    if not os.path.exists("semester_info.txt"):
        file_to_create = open("semester_info.txt", "w")
        file_to_create.close()
    file_io()
