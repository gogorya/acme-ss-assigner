import random


def _check(temp_list, list_to_shuffle, prev_year_dict):
    for i, j in zip(temp_list, list_to_shuffle):
        if i[1] == j[1] or (str(i[1]) in prev_year_dict and prev_year_dict[str(i[1])] == j[1]):
            return False
    return True


def assign(emp_list, prev_year_list):
    list_to_shuffle = emp_list[1:]
    temp_list = list(list_to_shuffle)
    random.shuffle(list_to_shuffle)

    prev_year_dict = {i[1]: i[3] for i in prev_year_list[1:]}

    attempts = 1
    while not _check(temp_list, list_to_shuffle, prev_year_dict):
        random.shuffle(list_to_shuffle)
        attempts += 1

    print("Total attempts to assign:", attempts)

    list_to_shuffle.insert(0, ['Secret_Child_Name', 'Secret_Child_EmailID'])

    merged_list = [i + j for i, j in zip(emp_list, list_to_shuffle)]

    return merged_list, attempts
