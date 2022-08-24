class Student:
    def __init__(self):
        self.collegeName = ("Harvard")
        self._major = ("History") #protected attribute
        self.__gpa = ("3.0") #private attribute

    def getGPA(self): # method utilizing private attribute in order to get information.
        print(self.__gpa)

    def setGPA(self, gpa): # method utilizing private attribute in order to change information.
        self.__gpa = gpa



james = Student() # creating object james, displaying information as well as changing gpa and displaying and displaying new gpa. 
print(james.collegeName)
print(james._major)
james.getGPA()
james.setGPA(4.0)
james.getGPA()






        

    


