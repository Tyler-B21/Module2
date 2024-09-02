#Tyler Bischoff
#M2Lab.py
#Program inputs student names/GPA
#Outputs students names/qualification for Dean's list and Honor Roll

#Variables
lname = ""
fname = ""
gpa = 0.0

#While loop Start
while lname != "ZZZ":
    #Intro
    print("""To check student's qualification for the Dean's List and Honor Roll, 
    enter student's last name, first name, and GPA. Enter ZZZ as the last name to quit processing student records.""")
    
    #Get inputs from user
    lname = input("Enter last name:")
    if lname == "ZZZ":
        break
    fname = input("Enter first name:")
    gpa = float(input("Enter GPA as a float:"))

    #Test inputs and output results
    if gpa >= 3.25:
        print(fname + " " + lname + " made the Dean's List!")
    elif gpa < 3.25:
        print(fname + " " + lname + " did not make the Dean's List or Honor's Roll")
    else:
        print("Error.")
    if gpa >= 3.5:
        print(fname + " " + lname + " made the Honor's Roll!")
#While loop End