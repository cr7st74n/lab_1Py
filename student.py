"""Cristian Gonzalez, 8/30/2023.This program will create a Student class that will have Name, ID and GPA """

from dataclasses import dataclass

#Compate to the traditional class , this is more easy to remember and write .
@dataclass
class student:
    name:str
    school_id :str
    gpa :float

    # # return the indormation of this class
    def __str__(self):
        return f'The information about the student: Name:{self.name}, ID:{self.school_id}, GPA:{self.gpa:.2f}'
    
    #Changhe the GPA with ta new one
    # def ChangeGPA( newGPA):
    #     gpa = newGPA

# main class that will add the information about the students :
def main():

    student1 = student("Cris", "123d45", 3.5)

    student2 = student("Tom", "234d43", 2.9)

    student3 = student("Mateo", "34g5ed", 3.9)

    student4 = student("Juan", "93jfw", 3.1)

    
    # student1.ChangeGPA(2.3)


    print(f' Students \n {student1} \n {student2} \n {student3} \n {student4} \n ')

main()