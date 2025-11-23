########################################################
# Task A10_T6
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import copy
import time
from typing import Callable

# --- Sorting algorithms ---
def bubbleSort(PNums: list[int]) -> None:
    """Bubble sort algorithm inplace."""
    n = len(PNums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]

def quickSort(PNums: list[int]) -> None:
    """Quick sort algorithm inplace."""
    def _quickSort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quickSort(arr, low, pivot_index - 1)
            _quickSort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quickSort(PNums, 0, len(PNums) - 1)

# --- Utility functions ---
def readValues(PValues: list[int]) -> None:
    """Read integers from file into list."""
    PValues.clear()
    filename = input("Insert dataset filename: ")
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line != "":
                    PValues.append(int(line))
        print(f"Dataset '{filename}' loaded with {len(PValues)} values.")
    except Exception as e:
        print(f"Error reading file: {e}")

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """Measure time in nanoseconds for sorting algorithm."""
    start = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    end = time.perf_counter_ns()
    return end - start

def saveResults(PResults: list[str]) -> None:
    """Save measured results to a file."""
    if not PResults:
        print("No results to save.")
        return
    filename = input("Insert results filename: ")
    try:
        with open(filename, 'w') as f:
            for line in PResults:
                f.write(line + '\n')
        print(f"Results saved to '{filename}'")
    except Exception as e:
        print(f"Error saving file: {e}")

# --- Menu functions ---
def showOptions() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

# --- Main ---
def main() -> None:
    print("Program starting.")
    Values: list[int] = []
    Results: list[str] = []
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            readValues(Values)
        elif choice == 2:
            if not Values:
                print("No dataset loaded. Please read dataset first.")
                continue
            print(f"Measured speeds for dataset ({len(Values)} values):")
            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f" - Built-in sorted {builtin_time} ns")
            print(f" - Bubble sort {bubble_time} ns")
            print(f" - Quick sort {quick_time} ns")
            Results = [
                f"Measured speeds for dataset ({len(Values)} values):",
                f" - Built-in sorted {builtin_time} ns",
                f" - Bubble sort {bubble_time} ns",
                f" - Quick sort {quick_time} ns"
            ]
        elif choice == 3:
            saveResults(Results)
        else:
            print("Unknown option!")
        print("")
    Values.clear()
    Results.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
