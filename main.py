import src.acme_ss_assigner as ss


def main():
    input_files = ss.parse_files()
    print("Processing:", input_files)

    emp_list = ss.read_file(input_files[0])
    prev_year_list = []
    if (len(input_files) == 2):
        prev_year_list = ss.read_file(input_files[1])

    assigned_list, attempts = ss.assign(emp_list, prev_year_list)
    print("Total attempts to assign:", attempts)

    output_file_name = input("Enter output file name: ")
    ss.write_file(output_file_name, assigned_list)

    # To check average attempts, uncomment following code
    '''
    total_attempts = 0
    iterations = 100 if len(emp_list) < 100000 else 10
    for i in range(iterations + 1):
        _, curr_attempts = ss.assign(emp_list, prev_year_list)
        total_attempts += curr_attempts

        bar_length = 20
        filled_length = int(bar_length * i // iterations)
        bar = "=" * filled_length + "-" * (bar_length - filled_length)
        print(f"[{bar}]", end="\r" if i < iterations else "\n", flush=True)

    average = round(total_attempts / iterations, 2)
    print("Average attempts:", average)
    '''


if __name__ == "__main__":
    main()
