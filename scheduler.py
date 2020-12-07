'''
Austin Sickels
12/6/20
'''


class Student:

    def __init__(self, name, time_week):
        self.username = name
        self.total_time_per_week = time_week


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

class ExamProject:

    def __init__(self, pe_name, c_name, date, time):
        self.name = pe_name
        self.class_name = c_name
        self.due_date = date
        self.time_to_complete = time

def read_user_input():
    student_name = input("Enter your name: ")
    student_hours = input(
        "Enter the hours you can study per week, excluding class time: ")
    semester_name = input("Enter semester and year: ")
    me = Student(student_name, student_hours)
    course_list = []
    while (True):
        course_name = input("Enter course name: ")
        course_credits = input("Enter number of credit hours: ")
        course_difficulty = input(
            "Enter projected course difficulty as a number between 1 and 100: ")
        course_confidence = input("How well do you know the material? 1-100: ")
        course = Course(course_name, course_credits, course_difficulty,
                        course_confidence)
        course_list.append(course)
        more_info = input(
            "Would you like to add more info for a better calculation? (y/n): ")
        if more_info == "y":
            professor_name = input("Enter professor\'s name: ")
            professor_difficulty = input("Enter professors\'s difficulty: ")
            passing_grade = input("Enter minimum grade for C-: ")
            course.set_optional_var(professor_name, professor_difficulty,
                                    passing_grade)
        exit_condition = input("Add another course? (y/n): ")
        if exit_condition == "n":
            break
    semester = Semester(semester_name, me, course_list)
    return semester

def file_io():
    file = open("semester_info.txt", "w+")
    fileIn = file.readline()
    if fileIn == "BEGIN":
        while fileIn != "END":
            fileIn = file.readline()
    else:
        file.write("BEGIN\n")
        file.write("END")


if __name__ == '__main__':
    file_io()
    out_semester = read_user_input()
    out_semester.print_semester()
