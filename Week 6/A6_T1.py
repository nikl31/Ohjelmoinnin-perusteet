def read(filename):
 
print("Program starting.")
print("This program can read a file.")
filename = input("Insert filename: ")

 file = open(filename, 'r', encoding="utf-8")
 while True:
   line = file.readline()
   if len(line) == 0:
    break
   line = line.strip()
   parts = line.split(';')
   print(f"Name: {parts[0]}, Height: {parts[1]}")
 file.close()