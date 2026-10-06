# Create and open a file in write mode
file = open("sample.txt", "w")

# Write content to the file
file.write("Hello, this is my first text file.\n")
file.write("I am learning Python file handling.\n")
file.write("Python is easy to learn.")

# Close the file
file.close()

print("Content written successfully!")