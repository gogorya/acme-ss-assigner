# Acme Assigner

This project is a random employee assigner built using Python and the Pytest framework (for testing). It operates using CSV files and adheres to the following rules:

- An employee cannot be assigned to themselves.
- An employee cannot be assigned to another employee who was assigned in the previous year's event, if applicable.
- Each employee must have exactly one assigned employee.
- Each employee should be assigned to only one employee.

## Functionality

- It works by shuffling the employee list and then testing if the assignment is valid.
- Based on testing, the average number of attempts typically hovers around 7 or 8.

## Getting Started

### Prerequisites

- `Python 3.x`
- `pip` (Python package installer)

### Installation

1. Clone the repository:

   ```sh
   git clone git@github.com:gogorya/acme-ss-assigner.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages (make sure the virtual environment is activated):

   ```bash
   pip install -r acme-ss-assigner/requirements.txt
   ```

## Usage

### Assign

```
python acme-ss-assigner/main.py current_year.csv [previous_year.csv]
```

### Run Tests

```
pytest -v
```

### Check Average Attempts

- To check average attempts, uncomment the commented code in `acme-ss-assigner/main.py`.

## CSV File Attributes

### Employee

```
Employee_Name,Employee_EmailID
```

### Previous Year & Ouput

```
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
```

## Other

- Make sure the Python interpreter is set to the virtual environment.
- Formatter used: [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8).
