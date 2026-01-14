# reader.py

from file_wr import write_numbers_to_file

def read_file_safely(filename):
    """
    Reads and prints the contents of a file safely with exception handling.
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File contents:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        # General fallback for any other I/O errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # First, write the numbers to file
    write_numbers_to_file("numbers.txt")

    # Then, read them
    read_file_safely("numbers.txt")

