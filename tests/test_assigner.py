import warnings

import pytest

from src.acme_ss_assigner import assign


# Testing emp_list length
@pytest.mark.parametrize("emp_list", [
    [],
    [["Employee_Name", "Employee_EmailID"]],
    [["Employee_Name", "Employee_EmailID"],
     ["John Doe", "john@doe.com"]]
])
def test_validate_emp_list_length(emp_list):
    with pytest.raises(ValueError, match="Employee list size is less than 2"):
        assign(emp_list, [])


# Testing RuntimeWarning with 2 items in emp_list against prev_year_list
def test_validate_list_lengths():
    emp_list = [["Employee_Name", "Employee_EmailID"],
                ["John Doe", "john@doe.com"],
                ["Jane Doe", "jane@doe.com"]]
    prev_year_list = [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
                      ["Person A", "a@doe.com", "Person B", "b@doe.com"],
                      ["Person B", "b@doe.com", "Person A", "a@doe.com"]]

    with pytest.warns(RuntimeWarning, match="Cannot use previous year list with only 2 employees"):
        assign(emp_list, prev_year_list)


# Testing emp_list format
@pytest.mark.parametrize("emp_list", [
    [["Employee_Namee", "Employee_EmailID"],
     ["John Doe", "john@doe.com"],
     ["Jane Doe", "jane@doe.com"],
     ["Person A", "a@doe.com"]],
    [["Employee_Name", "Employee_EmailIDD"],
     ["John Doe", "john@doe.com"],
     ["Jane Doe", "jane@doe.com"],
     ["Person A", "a@doe.com"]],
    [["Employee_Name"],
     ["John Doe", "john@doe.com"],
     ["Jane Doe", "jane@doe.com"],
     ["Person A", "a@doe.com"]],
    [["Employee_Name", "Employee_EmailID", "Secret_Child_Name"],
     ["John Doe", "john@doe.com"],
     ["Jane Doe", "jane@doe.com"],
     ["Person A", "a@doe.com"]],
    [["Employee_Name", "Employee_EmailID"],
     ["John Doe", "john@doe.com"],
     ["Jane Doe", "jane@doe.com"],
     ["Person A", "a@doe.com"],
     ["Person B"]]
])
def test_validate_emp_attributes(emp_list):
    with pytest.raises(ValueError, match="Employee list is not in proper format: "):
        assign(emp_list, [])


# Testing emp_list for duplicates
@pytest.mark.parametrize("emp_list", [
    [["Employee_Name", "Employee_EmailID"],
     ["John Doe", "john@doe.com"],
     ["Jane Doe", "jane@doe.com"],
     ["Person A", "john@doe.com"]]
])
def test_validate_emp_list_duplicates(emp_list):
    with pytest.raises(ValueError, match="Employee list containes duplicates: "):
        assign(emp_list, [])


# Testing prev_year_list format
@pytest.mark.parametrize("prev_year_list", [
    [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailIDd"]],
    [["Employee_Name", "Employee_EmailID" "Secret_Child_Name", "Secret_Child_EmailID"]],
    [["Employee_Name", "Employee_EmailID",
        "Secret_Child_Name", "Secret_Child_EmailID", ""]],
    [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
     ["Person A", "a@doe.com", "Person C", "c@doe.com"],
     ["Person B", "b@doe.com", "Person A", "a@doe.com"],
     ["Person C", "c@doe.com" "Person B", "b@doe.com"]],
    [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
     ["Person A", "a@doe.com", "Person C", "c@doe.com"],
     ["Person B", "b@doe.com", "Person A", "a@doe.com"],
     ["Person C", "c@doe.com", "Person B", "b@doe.com", ""]]
])
def test_validate_prev_year_attributes(prev_year_list):
    emp_list = [["Employee_Name", "Employee_EmailID"],
                ["John Doe", "john@doe.com"],
                ["Jane Doe", "jane@doe.com"],
                ["Person A", "a@doe.com"]]

    with pytest.raises(ValueError, match="Previous year list is not in proper format: "):
        assign(emp_list, prev_year_list)


# Testing prev_year_list for duplicates
@pytest.mark.parametrize("prev_year_list", [
    [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
     ["Person A", "a@doe.com", "Person C", "c@doe.com"],
     ["Person B", "c@doe.com", "Person A", "a@doe.com"],
     ["Person C", "c@doe.com", "Person B", "b@doe.com"]],
    [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
     ["Person A", "a@doe.com", "Person C", "c@doe.com"],
     ["Person B", "b@doe.com", "Person A", "a@doe.com"],
     ["Person C", "c@doe.com", "Person B", "a@doe.com"]]
])
def test_validate_prev_year_list_duplicates(prev_year_list):
    emp_list = [["Employee_Name", "Employee_EmailID"],
                ["John Doe", "john@doe.com"],
                ["Jane Doe", "jane@doe.com"],
                ["Person A", "a@doe.com"]]

    with pytest.raises(ValueError, match="Previous year list contains duplicates: "):
        assign(emp_list, prev_year_list)


# Testing RuntimeError on reaching maximum attempts
def test_max_attempts_error():
    emp_list = [["Employee_Name", "Employee_EmailID"],
                ["John Doe", "john@doe.com"],
                ["Jane Doe", "jane@doe.com"]]
    prev_year_list = [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
                      ["John Doe", "john@doe.com", "Jane Doe", "jane@doe.com"],
                      ["Jane Doe", "jane@doe.com", "John Doe", "john@doe.com"]]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        with pytest.raises(RuntimeError, match="Maximum attempts reached, please check input files"):
            assign(emp_list, prev_year_list)


# Testing the output of the assign function
def test_assign():
    emp_list = [["Employee_Name", "Employee_EmailID"],
                ["John Doe", "john@doe.com"],
                ["Jane Doe", "jane@doe.com"],
                ["Person A", "a@doe.com"],
                ["Person B", "b@doe.com"]]
    prev_year_list = [["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"],
                      ["John Doe", "john@doe.com", "Jane Doe", "jane@doe.com"],
                      ["Jane Doe", "jane@doe.com", "John Doe", "john@doe.com"],
                      ["Person A", "a@doe.com", "Person B", "b@doe.com"],
                      ["Person B", "b@doe.com", "Person A", "a@doe.com"]]

    assigned_list, _ = assign(emp_list, prev_year_list)
    assert assigned_list[0] == [
        "Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"]
    prev_year_dict = {i[1]: i[3] for i in prev_year_list[1:]}
    for i, j in zip(emp_list[1:], assigned_list[1:]):
        assert i[1] == j[1]
        assert j[1] != j[3]
        assert j[3] != prev_year_dict[str(i[1])]
