# Word Counter from Text File

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

        # Count characters
        characters = len(text)

        # Count words
        words = len(text.split())

        # Count lines
        lines = len(text.splitlines())

        print("\nFile Statistics")
        print("---------------")
        print("Number of Lines      :", lines)
        print("Number of Words      :", words)
        print("Number of Characters :", characters)

except FileNotFoundError:
    print("File not found!")