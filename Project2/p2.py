"""
File: py2.py
Author: Sina Roomi
Date: 11/18/2022
Lab Section: 43
Email:  sinar1@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

from dataEntryP2 import fillAttendanceData

# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!


def print_list(xlist):
    """
    When given a list, prints out elements in that list
    :param xlist: list given
    :return: element in the list
    """
    for element in xlist:
        print(element)


def print_list_small(xlist):
    """
    When given a list, prints out the first 6 and last 3
    :param xlist: list given
    :return: prints out elements in the list
    """
    for i in range(7):
        print(xlist[i])
    print(".........")
    for i in range(-1, -4,-1):
        print(xlist[i])

def connect_to_data_file(filename):
    # will return connection to data file
    infile = ""

    try:
        #infile = open("data.txt", "r")
        #infile = open("dataAllShow1stClass.txt", "r")
        infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file


def load_dictionary(data_file):
    """
    When given a data_file, the function takes the data and inserts it into a dictionary
    :param data_file: The data file given
    :return: a dictionary of the data from data_file
    """
    attendance_data = {}
    for line in data_file:
        #cleans up data form data_file
        my_string = line.strip().split(", ")
        name = ", ".join(my_string[0:2])
        #takes the name and stores it
        info_of_student = my_string[2:]

        #if the name is not already in the dict, it adds it
        if name not in attendance_data:
            attendance_data[name] = info_of_student
        #if the name is in the dict, it adds the new data to the existing data
        elif name in attendance_data:
            temp_list = [attendance_data[name], info_of_student]
            attendance_data[name] = temp_list
    return attendance_data


def print_dictionary(data):
    """
    When given a dictionary, the function prints out the data in it
    :param data: dictionary given to be printed out
    :return: prints out elements in data
    """
    for i in data:
        print(i, data[i])
        

def display_attendance_data_for_student(name, data):
    """
    When given a student name, prints out that student's information
    :param name: Student's name
    :param data: dictionary with all students information
    :return: Student's information
    """
    #checks if the name is in the data, if it is, prints the name and data
    if name in data:
        print(name,data[name]) 
    else:
        print("No student of this name in the attendance log.")


def is_present(name, date, data):
    """
    When given a student's name and a date, the function checks to see if the student
    was present for class
    :param name: student's name
    :param date: date the class was held
    :param data: dictionary with all student data
    :return: True or False if the student was present
    """
    data_of_student = data[name]
    present_or_not = False
    #checks the student's data and looks to see if the date given is in
    #if yes, present_or_not equals True
    for i in data_of_student:
        if date in i:
            present_or_not = True
    return present_or_not



def is_present_data(name, date, data):
    """
    When given a student's name and a date, the function checks to see if the student
    was present for class
    :param name: student's name
    :param date: date the class was held
    :param data: dictionary with all student data
    :return: Student's information
    """
    #this functions is the same as is_present but the only difference
    data_of_student = data[name]
    for i in data_of_student:
        if date in i:
            return (name, i)
    return ""


def list_all_students_checked_in(date, data):
    """
    When given a date, checks to see if students were present and puts
    present students into a list
    :param date: date the class was held
    :param data: dictionary with all student data
    :return: A list of all students who were present
    """
    list_of_checked_in = []
    for i in data:
        data_to_enter = is_present_data(i,date,data)
        if data_to_enter != "":
            list_of_checked_in.append(i)
    return list_of_checked_in


def converter(timestamp):
    """
    When given a timestamp, it splits the string and returns the timestamp(string) as seconds(int)
    :param timestamp: Timestamp that is going to be converted into seconds
    :return: total amount of seonds from the given timestamp
    """
    total_seconds = 0
    #strips and cleans the string timestamp into just a number with nothing around it
    time_string = timestamp.strip("['").strip("']").split(":")
    #takes the string and slices it from right to left and adds it to total seconds

    total_seconds += (int(time_string[0]) * 60 * 60) + (int(time_string[1]) * 60) + int(time_string[2])

    """
    for i in range(2,-1,-1):   
        if time_string[i] == time_string[2]:
            total_seconds += int(time_string[i])
        elif time_string[i] == time_string[1]:
            total_seconds += int(time_string[i]) * 60
        elif time_string[i] == time_string[0]:
            total_seconds += int(time_string[i]) * 60 * 60
    """
    return total_seconds


def list_all_students_checked_in_before(date, time, data):
    """
    When given a date and time, checks for present students and
    if they checked in before the time given.
    :param date: date the class was held
    :param time: The time given for the check
    :param data: dictionary with all student data
    :return: True or False if the student was present
    """
    list_to_return = []
    #converts the time given to seconds
    time_in_seconds = converter(time)
    #gets list of all present students
    list_of_attended_name = list_all_students_checked_in(date,data)
    #Check to see if the students arrived before the listed time
    for i in list_of_attended_name:
        student = data[i]
        student_time = converter(student[0][0])
        if student_time < time_in_seconds:
            list_to_return.append(i)
    return list_to_return




def find_number_of_classes_student(information, data):
    """
    When given a date, finds the first student to enter that day
    :param information: student's name
    :param data: dictionary with all student data
    :return: the number of classes a student attended
    """
    count = 0
    for i in data[information]:
        for j in i:
            count +=1
    return count//2
    
    

def attended_both_class(data, amount_of_classes):
    """
    When given the amount of classes to check for, the function returns
    a list of those students that met the requirement
    :param data: dictionary with all student data
    :return: the number of classes a student attended
    """
    list_of_attended = []
    count_of_classes = 0
    for name in data:
        count_of_classes = find_number_of_classes_student(name,data)
        if count_of_classes == amount_of_classes:
            list_of_attended.append(name)
        count_of_classes = 0

    return list_of_attended

#didn't see this function on the google doc form so I don't have a print statment for it
def attended_one_class(data):
    """
    When given data, puts the students that only attend one class into a list
    :param data: dictionary with all student data
    :return: a list of students that only attend once
    """
    list_of_one = []
    count_of_classes = 0
    for name in data:
        count_of_classes = find_number_of_classes_student(name,data)
        if count_of_classes == 1:
            list_of_one.append(name)
        count_of_classes = 0
    return list_of_one

#didn't see this function on google doc form so I don't have a print statement for it
def attended_no_class(data, classRoster):
    """
    When given data and a class roster, checks for students that didn't attend class
    :param data: dictionary with all student data
    :return: a list of absent students
    """
    list_of_absent = []
    for name in classRoster:
        if name not in data:
            list_of_absent.append(name)
    return list_of_absent

def get_first_student_to_enter(date, data):
    """
    When given a date, finds the first student to enter that day
    :param date: date the class was held
    :param data: dictionary with all student data
    :return: the name of the earliest student
    """
    list_of_students = list_all_students_checked_in(date,data)
    earliest_time = converter(data[list_of_students[0]][0][0])
    earliest_student = list_of_students[0]
    for i in list_of_students:
        data_of_student = data[i]
        try:
            time_of_student = converter(data_of_student[0][0])
        except IndexError:
            time_of_student = converter(data_of_student[0])
        if time_of_student < earliest_time:
            earliest_time = time_of_student
            earliest_student = i
    return earliest_student


def print_count(given_list):
    """
    When given a list, counts each element in the list
    :param given_list: given list 
    :return: a printed statement and the count
    """
    count = 0
    for i in given_list:
        count += 1
    return print(f"There were {count} records for this query")


def load_roster(roster_file_name):
    """
    When give a file, it loads it a puts the information into a list
    :param roster_file_name: the file's name
    :return: a list of information from that file
    """
    second_data = connect_to_data_file(roster_file_name)
    class_list = []
    for names in second_data:
        class_list.append(names.strip())
    return class_list
    
if __name__ == '__main__':

    """
    infile = connect_to_data_file("randomData.txt")
    if(infile):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)"""
    the_file_name = 'dataALLShow1stAnd2ndClass.txt'
    infile = connect_to_data_file(the_file_name)
    if(infile):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary(infile)

    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
    #print_dictionary(data)
    
    #imports rosters.txt
    second_file_name = "rosters.txt"
    classRoster = load_roster(second_file_name)


    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)

    
    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/17/2022", data))

    
    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    #print_list will print out the entire list
    #print_list(result)
    #print_list_small shows first 6 and last 3
    print_list_small(result)
    print_count(result)
    
    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)

    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    result = attended_both_class(data, 2)
    #print_list will print out the entire list
    #print_list(result)
    #print_list_small shows first 6 and last 3
    print_list_small(result)
    print_count(result)

    print("**** First student to enter on 11/2/2022 ****")
    print(get_first_student_to_enter("11/2/2022", data))
    print("**** First student to enter on 11/3/2022 ****")
    print(get_first_student_to_enter("11/3/2022", data))
    print("**** First student to enter on 11/4/2022 ****")
    print(get_first_student_to_enter("11/4/2022", data))
    print("**** First student to enter on 11/5/2022 ****")
    print(get_first_student_to_enter("11/5/2022", data))