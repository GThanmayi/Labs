def write_numbers_to_file(filename):
    """
    Writes the numbers 1–100 into the text file named filename.
    Handles file-related exceptions gracefully.
    """
    try:
        with open(filename, "w") as file:
            for num in range(1, 101):
                file.write(str(num) + "\n")
        print(f"Successfully wrote numbers 1–100 to '{filename}'")

    except FileNotFoundError:
        print(f"Error: The path for '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied. Cannot write to '{filename}'.")

    except OSError as e:
        # Handles other I/O exceptions (e.g., disk full, invalid filename)
        print(f"An I/O error occurred: {e}")
