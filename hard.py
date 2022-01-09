"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine
if their course can be taken or not.

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge.
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json
import re
from distutils.util import strtobool

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()


def process_condition(condition):

    """
    Cleans the incoming condition text
    """
    # Clean conditions text

    # Remove excess spaces
    condition = ' '.join(condition.split())

    #Replace lowercase and, or statements
    condition = condition.replace("AND", "and").replace("OR", "or")

    #Remove full stops at the end of conditions
    condition = condition.replace(".", "")

    #Replace "prerequisite"
    prereq_replace = {
        "Pre-requisite": "",
        "Prerequisite": "",
        "Pre-req": "",
        "Prequsite": ""
    }
    for key in prereq_replace:
        condition = condition.replace(key, prereq_replace[key])

    #Course entry mistakes
    course_replace = {
        "4951": "COMP4951",
        "4952": "COMP4952",
        "COMP64443": "COMP6443"
    }

    for key in course_replace:
        condition = condition.replace(key, course_replace[key])

    #Miscellaneous mistakes
    condition = condition.replace("oc", "of")
    condition = condition.replace("Completion of", "").replace("completion of", "")
    condition = condition.replace(":", "")

    return condition



def check_uoc_selection(condition):
    """
    Checks condition for "x units of credit in (<courses>)"
    """
    if " units of credit in (" in condition:
        condition_split = condition.split(" units of credit in ")
        uoc = condition_split[0].split()[-1]
        courses_to_check = condition_split[1][condition_split[1].find("(") + 1 : condition_split[1].find(")")]
        courses_to_check_list = courses_to_check.split(", ")
        courses_to_check_list = [bool(strtobool(bool_val)) for bool_val in courses_to_check_list]

        #Replaces the string in question with a boolean
        string_to_replace = uoc + " units of credit in (" + courses_to_check + ")"
        if 6 * sum(courses_to_check_list) >= int(uoc):
            condition = condition.replace(string_to_replace, "True")
        else:
            condition = condition.replace(string_to_replace, "False")

    return condition

def check_comp_uoc_level(courses_list, condition):
    """
    Checks whether a student has completed a certain number of UOC
    of COMP courses for a given level
    """
    if " units of credit in level " in condition:
        condition_split = condition.split(" units of credit in level ")
        uoc_required = condition_split[0].split()[-1]
        level = condition_split[1].split()[0]

        string_to_replace = uoc_required + " units of credit in level " + level + " COMP courses"

        uoc_completed = 0
        for course in courses_list:
            if int(course[4]) == int(level):
                uoc_completed += 6

        if uoc_completed >= int(uoc_required):
            condition = condition.replace(string_to_replace, "True")
        else:
            condition = condition.replace(string_to_replace, "False")

    return condition

def check_uoc(courses_list, condition):

    """
    Checks whether a student has completed a certain number of UOC
    """

    if " units of credit" in condition:
        condition_split = condition.split(" units of credit")
        uoc = condition_split[0].split()[-1]
        string_to_replace = uoc + " units of credit"

        if 6 * len(courses_list) >= int(uoc):
            condition = condition.replace(string_to_replace, "True")
        else:
            condition = condition.replace(string_to_replace, "False")

    return condition

def evaluate_condition(condition, courses_list):

    """
    Evaluates a given condition against a given list of courses
    """

    #SImple case, where there is no prerequisite
    if condition == "":
        return True

    #Splits the condition string into words and punctuation
    condition = re.split('(\W)', condition)

    #Identifies the course codes in the split condition and checks if
    #they are already in the courses_list
    for i,word in enumerate(condition):
        if len(word) == 8:
            if word[4:8].isnumeric():
                #Replaces course code with either True or False
                if word in courses_list:
                    condition[i] = "True"
                else:
                    condition[i] = "False"

    condition = ''.join([item for item in condition])

    #Check for "x units of credit in (<courses>)"
    condition = check_uoc_selection(condition)

    #Check for "x units of credit in level y COMP courses"
    condition = check_comp_uoc_level(courses_list, condition)

    #Check for "x units of credit" - note that this is done last
    #to prevent the code from changing the text when one of the previous
    #two cases are found
    condition = check_uoc(courses_list, condition)

    #Evaluates an expression of booleans to give an overall boolean value
    return eval(condition)


def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course
    can be unlocked by them.

    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """

    processed_condition = process_condition(CONDITIONS[target_course])
    evaluated_condition = evaluate_condition(processed_condition, courses_list)

    return evaluated_condition
