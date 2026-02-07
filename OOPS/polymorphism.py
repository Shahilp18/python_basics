
#! Polymorphism
#* mony forms

#* Function Ovveriding
 
class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
     def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()

#* Duck Typing 
 
class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
     def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()