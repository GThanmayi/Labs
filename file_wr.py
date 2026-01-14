# file_writer.py

def write_numbers_to_file(filename):
    """
    Writes the numbers 1–100 into a text file named filename.
    """
    with open(filename, "w") as file:
        for num in range(1, 101):
            file.write(str(num) + "\n")
