'''
Austin Sickels
12/6/20
'''


class User:

    def __init__(self, name, time_week):
        self.username = name
        self.total_time_per_week = time_week


class Course:

    def __init__(self, name, credits, difficulty, confidence):
        self.course_name = name
        self.course_credts = credits
        self.course_difficulty = difficulty
        self.confidence = confidence


class Semester:

    def __init__(self, name, user, list_of_courses):
        self.semester_name = name
        self.student = user
        self.course_list = list_of_courses

    def print_semester(self):
        print(f"Semester: {self.semester_name}")
        print(f"Student: {self.student.username}")
        print("Courses", end=": ")
        for course in self.course_list:
            print(course.course_name, end=" ")
        print()




if __name__ == '__main__':
    me = User("Austin", 3)
    course1 = Course("CS311", 3, 70, 50)
    course2 = Course("CS363", 3, 30, 80)
    course3 = Course("CS321", 3, 70, 50)
    course4 = Course("CS327", 3, 70, 50)
    courses = [course1, course2, course3, course4]
    semester = Semester("Fall2020", me, courses)
    semester.print_semester()
