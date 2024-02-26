class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def printName(self):
        name = self.firstname + " " + self.lastname
        return name
    
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject
    def printNameSubject(self):
        name = self.printName()
        nameSubject = name + ", " + self.subject
        return nameSubject
    
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super(Teacher, self).__init__(firstname, lastname)
        self.course = course
    def printNameCourse(self):
        name = self.printName()
        nameCourse = name + ", " + self.course
        return nameCourse
