def write_numbers_to_file(filename):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write numbers 1 through 10, each on a new line
        for num in range(1, 11):
            file.write(str(num) + "\n")
