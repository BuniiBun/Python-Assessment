import json
import Functions

#Create Dictionaries
#StudentsDict["students"][0]["id"] - Indexing StudentDict Information Example
StudentsDict = Functions.CSVtoDict("students.csv")
MarksDict = Functions.CSVtoDict("marks.csv")
TestsDict = Functions.CSVtoDict("tests.csv")
CoursesDict = Functions.CSVtoDict("courses.csv")

#Calculate Student Averages
for Student in StudentsDict["students"]:
    StudentID = int(Student["id"])
    StudentMarks = []
    for TestMark in MarksDict["marks"]:
        if (int(TestMark["student_id"])) == StudentID:
            StudentMarks.append(int(TestMark["mark"]))

    Student["totalAverage"] = round(Functions.CalculateAvg(StudentMarks), 2)

#Get Student Courses
for Student in StudentsDict["students"]:
    StudentID = int(Student["id"])
    Courses = []
    ###Loop Through Marks To Find Tests
    for TestMark in MarksDict["marks"]:
        if (int(TestMark["student_id"])) == StudentID:
            TestID = int(TestMark["test_id"])
    ###Loop Through Tests To Find Course
            for Test in TestsDict["tests"]:
                if (int(Test["id"])) == TestID:
                    CourseID = int(Test["course_id"])
    ###Loop Through Courses To Build List
                    for Course in CoursesDict["courses"]:
                        if (int(Course["id"])) == CourseID:
                            CourseList = {}
                            CourseList["id"] = CourseID
                            CourseList["name"] = Course["name"]
                            CourseList["teacher"] = Course["teacher"]
                            Courses.append(CourseList)

    #Clean Courses And Remove Duplicates
    Seen = set()
    NewCourseList = []
    for Course in Courses:
        t = tuple(Course.items())
        if t not in Seen:
            Seen.add(t)
            NewCourseList.append(Course)

    #Implement Course Data Into Student Dictionary
    Student["courses"] = NewCourseList

    #Get Course Average
    for Course in Student["courses"]:
        CourseID = int(Course["id"])
        #Get Tests For That Course
        CourseMarks = []
        for Test in TestsDict["tests"]:
            if int(Test["course_id"]) == CourseID:
                TestID = int(Test["id"])
                for Mark in MarksDict["marks"]:
                    if int(Mark["test_id"]) == TestID:
                        CourseMarks.append(int(Mark["mark"]))

        Course["courseAverage"] = round(Functions.CalculateAvg(CourseMarks), 2)


#JSON Dump To New File
"""
with open("StudentData.json", "w") as Output:
    json.dump(StudentsDict, Output, indent = 3)
"""