import sys

import src.acme_ss_assigner as ss


def main():
    try:
        input_files = ss.parse_files()
        print("Processing:", input_files)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    emp_list = ss.read_file(input_files[0])

    assigned_list = ss.assign(emp_list)

    output_file_name = input("Enter output file name: ")

    ss.write_file(output_file_name, assigned_list)


if __name__ == "__main__":
    main()
