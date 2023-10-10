debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data


def list_students_not_in_class(classRoster, attendData):
    """
    Compare the swipe log with the given course roster. Place those students that
    did not show up for class into a list.
    :param classRoster: a list of names (last, first)
    :param attendData: List of all swipe data 
    :return: List of students that did not swipe in for class
    """
    #make a new list with only the names from attendData
    attended_names = []
    for data in attendData:
        attended_names.append(", ".join(data.split(", ")[:2]))
    
    #check if those names from attendData match up with list of names provided by classRoster and if they don't, add them to miss_student
    missing_students = []
    for student in classRoster:
        if student not in attended_names:
            missing_students.append(student)
   
    return missing_students


def list_all_times_checking_in_and_out(name_of_student, attendData):
    """
    Looking at the swiping log, this function will list all in and outs for a
    particular Student. Please note, as coded in the p1.py file given, this
    function was called three times with different student values. 
    :param name_of_student: the name of the student we want to look for 
    :param attendData: List of all swipe data 
    :return: list of all information about the student that was provided in the attendData
    """

    list_of_names = []
    list_of_timestamps = []
    list_of_dates = []
    list_of_results = []

    sign_in = False
    sign_out = False
    count = 0
    #these 3 for loops seperates the information from attendData into 3 list, last+first name, time, and date
    for names in attendData:
        new_list = names.split(", ")
        new_list = ", ".join(new_list[:2])
        list_of_names.append(new_list)

    for timestamps in attendData:
        new_list = timestamps.split(", ")
        new_list = ", ".join(new_list[2:3])
        list_of_timestamps.append(new_list)

    for dates in attendData:
        new_list = dates.split(", ")
        new_list = ", ".join(new_list[3:])
        list_of_dates.append(new_list)
    
    for name in list_of_names:
        #checks to see if there is repeat
        if name == name_of_student:
            count +=1
            #if there is one repeat, that means they signed in
            if count == 1:
                sign_in = True
                first_spot = list_of_names[list_of_names.index(name)]
                first_time_spot = list_of_timestamps[list_of_names.index(name)]
                first_date_spot = list_of_dates[list_of_names.index(name)]
                list_of_names.remove(name)
            #if there is two repeats, that means they also signed out
            if count == 2:
                sign_out = True
                second_spot = list_of_names[list_of_names.index(name)]
                second_time_spot = list_of_timestamps[list_of_names.index(name)+1]
                second_date_spot = list_of_dates[list_of_names.index(name)+1]

    #if they signed in, add the information to the list
    if sign_in == True:
        list_of_results.append(first_spot)
        list_of_results.append(first_time_spot)
        list_of_results.append(first_date_spot)
    # if they signed out, also add that information to the list
    if sign_out == True:
        list_of_results.append(second_spot)
        list_of_results.append(second_time_spot)
        list_of_results.append(second_date_spot)
    #if they never signed in or out, that means theres no information for this person in attendData
    if sign_in == False and sign_out == False:
        list_of_results.append("No data for this person.")
    
        
    return list_of_results

    
def list_all_times_checked_in(attendData):
    """
    This function returns a list of when all student(s) FIRST swipe in. 
    :param attendData: List of all swipe data  
    :return: list of students when they first swipe in
    """    
    list_of_names = []
    list_of_timestamps = []
    list_of_dates = []
    list_of_results = []

    #these 3 for loops seperates the information from attendData into 3 list, last+first name, time, and date
    for names in attendData:
        new_list = names.split(", ")
        new_list = ", ".join(new_list[:2])
        list_of_names.append(new_list)

    for timestamps in attendData:
        new_list = timestamps.split(", ")
        new_list = new_list[2:3]
        list_of_timestamps.append(new_list)

    for dates in attendData:
        new_list = dates.split(", ")
        new_list = ", ".join(new_list[3:])
        list_of_dates.append(new_list)

    list_of_indexes = []
    list_of_already_found = []
    count = 0 
    for name in list_of_names:
        #if the name from list_of_names is not already in list_of_already_found, add it and add the index of it to list_of_indexes
        if name not in list_of_already_found:
            list_of_already_found.append(name)
            list_of_indexes.append(count)
        count += 1
    #combine and append the information that was provided by list_of_indexes
    for i in list_of_indexes:
        a = f"{list_of_names[i]}, {list_of_timestamps[i]}, {list_of_dates[i]}"
        list_of_results.append(a)

    return list_of_results


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
    for i in range(2,-1, -1):
        if time_string[i] == time_string[2]:
            total_seconds += int(time_string[i])
        elif time_string[i] == time_string[1]:
            total_seconds += int(time_string[i]) * 60
        elif time_string[i] == time_string[0]:
            total_seconds += int(time_string[i]) * 60 * 60
    return total_seconds
    

def list_students_late_to_class(time, attendData):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param time: the time where students swipe after are considered late 
    :param attendData: List of all swipe data 
    :return: List of students that showed up to class late
    """ 
    #brings data from list_all_times_checked_in()
    list_of_sign_in = list_all_times_checked_in(attendData)
    list_of_late = []
    for i in list_of_sign_in:
        #takes {time} and timestamp from list_of_sign_in and makes it into total seconds
        split_data = i.split(", ")
        conversion1 = converter(split_data[2])
        conversion2 = converter(time)
        #see if the timestamp from ist_of_sign_in is greater than {time} and if it is, it adds it to a list
        if conversion1 > conversion2:
            list_of_late.append(", ".join(split_data))
    return list_of_late


def get_first_student_to_enter(attendData):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param attendData: List of all swipe data 
    :return: earliest student to sign in
    """ 
    #brings data from list_all_times_checked_in() 
    list_of_sign_in = list_all_times_checked_in(attendData)
    list_of_times = []
    #splits the data from list_of_sign_in and converts it to total seconds
    for i in list_of_sign_in:
         for i in list_of_sign_in:
            split_data = i.split(", ")
            conversion = converter(split_data[2])
            list_of_times.append(conversion)

    #compares the total seconds and makes temp_var the smallest value from the list
    temp_var = list_of_times[0]
    for i in range(len(list_of_times)-1):
        if temp_var > list_of_times[i]:
            temp_var = list_of_times[i]
    return list_of_sign_in[list_of_times.index(temp_var)]
    

def printList(given_list):
    for i in given_list:
        print(i, end = '\n')

    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param given_list: A list 
    :return: prints out the list given
    """

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    
    
    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here
    
    #load data
    attendData = fill_attendance_data()
    
    #use different tests 
    # make sure roster was filled 
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)


    #list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData)) 
    #display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    #display first student to enter class
    print("******* Get 1st student to enter class ****************")    
    print(get_first_student_to_enter(attendData))
