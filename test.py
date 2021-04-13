class Student(object):
    name = ""
    schoollevel = ""
    studentID = ""
    currentCreditHours = ""
    currentGPA = ""
    desiredGPA = ""
    remainingCreditHours = ""
    takingClasses = ""
    numOfClasses = ""
    classesName = [""]
    classesGrade = ['']
    classesHours = []



    

def create_student():
    newstudent = Student()
    
    #makes the name
    newstudent.name = input("What is your name?: \n")


    #makes the schoollevel
    check1 = False
    while not check1:
        newstudent.schoollevel = input("Are you in High school or College?: \n")
        if newstudent.schoollevel.upper() == "HIGH SCHOOL":
            check1=True
            newstudent.schoollevel = 'HIGH SCHOOL'
            break
        elif newstudent.schoollevel.upper() == "COLLEGE":
            check1=True
            newstudent.schoollevel = "COLLEGE" 
            break     
        else:
            print("Please put 'High School' or 'College'")

    #makes the studentID if user is in college
    if newstudent.schoollevel == "COLLEGE":
        newstudent.studentID = input("What is your studentID? \n")
    else:
        newstudent.studentID = "N/A"

    
    #Sees how many credit hours/GPA a student has already taken
    newstudent.currentCreditHours = int(input("How many credit hours have you taken? (Not including classes you are currently taking):  \n"))
    newstudent.currentGPA = float(input("What is your current GPA? (Not including classes you are currently taking):  \n"))
    newstudent.desiredGPA = float(input("What is your desired GPA:  \n"))
    newstudent.remainingCreditHours = int(input("How many credit hours do you have remaining (Not including classes you are currently taking):  \n"))

    
    #asks if you are currently taking classes
    check2 = 0
    while check2 < 1:
        newstudent.takingClasses = input("Are you currently taking classes? (Yes or No)  \n")
        if newstudent.takingClasses.upper() == "YES" or newstudent.takingClasses.upper() == "NO":
            check2 = 1
            newstudent.takingClasses == newstudent.takingClasses.upper()
        else:
            print("incorrect format")


    #Checks to see how many classes a person is taking
    newstudent.numOfClasses = 0
    if newstudent.takingClasses.upper() == "YES":
        newstudent.numOfClasses = int(input("How many classes are you taking?  \n"))
    

    #Gets the list of classes
    for i in range(newstudent.numOfClasses):
        newstudent.classesName = [input("Put the name of a class you are taking. \n")]
        newstudent.classesGrade = [input("What letter grade do you plan to make? \n")]
        newstudent.classesHours = [input("How many credit hours will you receive for this class? \n")]

    return newstudent.name, newstudent.schoollevel, newstudent.studentID, newstudent.currentCreditHours, \
        newstudent.currentGPA, newstudent.desiredGPA, newstudent.remainingCreditHours, \
            newstudent.takingClasses, newstudent.numOfClasses, newstudent.classesName, newstudent.classesGrade, newstudent.classesHours

name, schoollevel, studentID, currentCreditHours, \
        currentGPA, desiredGPA, remainingCreditHours, \
            takingClasses, numOfClasses, classesName, classesGrade, classesHours = create_student()


#Using the 3 differnt grading scales to determine their GPA from the courses above based off quality hours 
def letters():
    qualityPoints = 0
    listGrades = []
    listCreditHours = []
    print(classesGrade)  #This is a temp variable to see if things are working
    if takingClasses == "YES":

        for i in range(numOfClasses):
            beValid = False
            while not beValid:
            
                if classesGrade == "A" or classesGrade == "a" or classesGrade == "4" or int(classesGrade) >= 90:
                    beValid = True
                    classInput1 = 4
                elif classesGrade == "B":
                    beValid = True
                    classInput1 = 3
                elif classesGrade == "C":
                    beValid = True
                    classInput1 = 2
                elif classesGrade == "D":
                    beValid = True
                    classInput1 = 1
                elif classesGrade == "F":
                    beValid = True
                    classInput1 = 0
        qualityPoints += (classInput1*classesHours)
        listGrades.append(classInput1)
        listCreditHours.append(classesHours)

    return classesHours


letters()

