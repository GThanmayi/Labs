def write_numbers_to_file(numbers):
    with open(numbers,"w") as file:
        for num in range(1,101):
            file.write(str(num)+ "\n")
