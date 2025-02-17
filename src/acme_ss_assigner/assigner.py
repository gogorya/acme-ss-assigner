import random
import warnings

from itertools import islice


# Validating input data
def _validate(emp_list, prev_year_list):
    # Checking lists' lengths
    if len(emp_list) <= 2:
        raise ValueError("Employee list size is less than 2")
    elif len(emp_list) == 3 and len(prev_year_list) >= 3:
        warnings.warn(
            "Cannot use previous year list with only 2 employees", RuntimeWarning)

    # Verifying emp_list format and checking for duplicates
    expected_emp_attributes = ["Employee_Name", "Employee_EmailID"]
    if len(emp_list[0]) != 2 or emp_list[0] != expected_emp_attributes:
        raise ValueError(
            "Employee list is not in proper format: " + str(emp_list[0]))
    for i in range(len(emp_list)):
        if len(emp_list[i]) != 2:
            raise ValueError(
                "Employee list is not in proper format: " + str(i + 1) + ": " + str(emp_list[i]))
    seen = set()
    for i in range(len(emp_list)):
        if emp_list[i][1] in seen:
            raise ValueError("Employee list containes duplicates: " +
                             str(i + 1) + ": " + str(emp_list[i]))
        else:
            seen.add(emp_list[i][1])

    # Verifying prev_year_list format and checking for duplicates
    if len(prev_year_list):
        expected_prev_attributes = [
            "Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"]
        if len(prev_year_list[0]) != 4 or prev_year_list[0] != expected_prev_attributes:
            raise ValueError(
                "Previous year list is not in proper format: " + str(prev_year_list[0]))
        for i in range(len(prev_year_list)):
            if len(prev_year_list[i]) != 4:
                raise ValueError(
                    "Previous year list is not in proper format: " + str(i + 1) + ": " + str(prev_year_list[i]))
    seen.clear()
    seen_as = set()
    for i in range(len(prev_year_list)):
        if prev_year_list[i][1] in seen or prev_year_list[i][3] in seen_as:
            raise ValueError("Previous year list contains duplicates: " +
                             str(i + 1) + ": " + str(prev_year_list[i]))
        else:
            seen.add(prev_year_list[i][1])
            seen_as.add(prev_year_list[i][3])


# Checking if shuffled list is valid
def _check(temp_list, list_to_shuffle, prev_year_dict):
    for i, j in zip(temp_list, list_to_shuffle):
        if i[1] == j[1] or (str(i[1]) in prev_year_dict and prev_year_dict[str(i[1])] == j[1]):
            return False
    return True


# Main assignment function
def assign(emp_list, prev_year_list):
    # Validating the lists
    _validate(emp_list, prev_year_list)

    # Creating lists for operations
    list_to_shuffle = [i for i in islice(emp_list, 1, None)]
    temp_list = list(list_to_shuffle)
    random.shuffle(list_to_shuffle)

    # Dictionary to check previous year assignments
    prev_year_dict = {i[1]: i[3] for i in islice(prev_year_list, 1, None)}

    # Checking if the shuffled list is valid
    attempts = 1
    max_attempts = 200 if len(emp_list) < 100000 else 50
    while not _check(temp_list, list_to_shuffle, prev_year_dict) and attempts < max_attempts:
        random.shuffle(list_to_shuffle)
        attempts += 1
    if attempts == max_attempts:
        raise RuntimeError(
            "Maximum attempts reached, please check input files")

    # Generating list with assigned entities
    list_to_shuffle.insert(0, ['Secret_Child_Name', 'Secret_Child_EmailID'])
    merged_list = [i + j for i, j in zip(emp_list, list_to_shuffle)]

    return merged_list, attempts
