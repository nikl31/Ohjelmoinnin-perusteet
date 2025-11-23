def showMenu():
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def drawSquare(dwg):
    print("Insert square details:")
    x = int(input("Top-left X: "))
    y = int(input("Top-left Y: "))
    size = int(input("Side length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    dwg.add(dwg.rect(insert=(x, y), size=(size, size), fill=fill, stroke=stroke))

def drawCircle(dwg):
    print("Insert circle details:")
    cx = int(input("Center X: "))
    cy = int(input("Center Y: "))
    r = int(input("Radius: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    dwg.add(dwg.circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))

def drawHexagon(dwg):
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    # circumradius
    R = apothem * 2 / math.sqrt(3)
    points = []
    for i in range(6):
        angle_deg = 30 + i * 60  # start from top-right corner
        angle_rad = math.radians(angle_deg)
        x = cx + R * math.cos(angle_rad)
        y = cy - R * math.sin(angle_rad)  # SVG y-axis is top-down
        points.append((round(x), round(y)))
    dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke))

def main():
    print("Program starting.")
    dwg = svgwrite.Drawing(size=("500px", "500px"))
    
    while True:
        showMenu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        elif choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            drawHexagon(dwg)
        elif choice == "4":
            filename = input("Insert filename: ")
            confirm = input(f'Save file to "{filename}"? Proceed (y/n)?: ')
            if confirm.lower() == "y":
                dwg.saveas(filename)
                print("Vector saved successfully!")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
