try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes leading/trailing whitespace
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found. Please check the filename and try again.")
