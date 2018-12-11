class Member :
    def __init__(self,full_name):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi, my name is {self.full_name}!")

class Student(Member):
    def __init__(self,full_name,reason):
        super().__init__(full_name)
        self.reason = reason
    
    def __str__(self):
        return 'student'

class Instructor(Member):
    def __init__(self,full_name,bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []
    
    def add_skill(self,skill):
        self.skills.extend([skill])
    
    def __str__(self):
        return 'instructor'
class Workshop :
    def __init__(self,date,subject):
        self.date = date
        self.subject = subject
        self.instructor = []
        self.students = []
    
    def add_participant(self,member):
        if str(member)=='student':
            self.students.append(member)
        elif str(member)=='instructor':
            self.instructor.append(member)
    def print_details(self):
        print(f"This workshop teaches {self.subject} starts in {self.date} ")




workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()