print("Program starting")
print("Estimate how many minutes you spent on programming...")
task1 = int(input("A1_T1:"))
task2 = int(input("A1_T2:"))
task3 = int(input("A1_T3:"))
task4 = int(input("A1_T4:"))
task5 = int(input("A1_T5:"))
task6 = int(input("A1_T6:"))
task7 = int(input("A1_T7:"))
total = task1 + task2+ task3 + task4 + task5 + task6 + task7
average = total/7
print(f'Average per task was {round(average,2)} min and same rounded to the nearest integar {round(average)} min.')
print("Program ending")