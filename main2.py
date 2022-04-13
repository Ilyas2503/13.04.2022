class Student:


    def __init__(self,name, last_name, year_of_entrance, department):
        self.name = name
        self.last_name = last_name
        self.year_of_entrance = year_of_entrance
        self.department = department


    def get_student_info(self):
        print (f" your name {self.name},{self.last_name},{self.year_of_entrance}, {self.department} ")


a = Student("Ilyas", "Abdyzhaparov", 2022, "Python")
a.get_student_info()
