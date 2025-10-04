print("Program starting.\n")

print("Check multiplicative persistence.")
n = input("Insert an integer: ")

steps = 0

while len(n) > 1:
    digits = [int(d) for d in n]
    product = 1
    for d in digits:
        product *= d
    print(" * ".join(n), "=", product)
    n = str(product)
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")
