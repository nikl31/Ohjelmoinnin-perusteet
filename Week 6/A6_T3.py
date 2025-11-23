print("Program starting.")
print("This program can copy a file.")

source_file = input("Insert source filename: ")
dest_file = input("Insert destination filename: ")

try:
    print(f"Reading file '{source_file}' content.")
    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()
    print("File content ready in memory.")

    print(f"Writing content into file '{dest_file}'.")
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(content)

    print("Copying operation complete.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Program ending.")
