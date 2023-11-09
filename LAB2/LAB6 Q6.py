def calculate_area(length, width):
    return length * width


num_rectangles = int(input("Enter the number of rectangles: "))

lengths = []
widths = []

for i in range(num_rectangles):
    length = float(input(f"Enter the length of rectangle {i + 1}: "))
    width = float(input(f"Enter the width of rectangle {i + 1}: "))
    lengths.append(length)
    widths.append(width)

areas = [calculate_area(length, width) for length, width in zip(lengths, widths)]

print("\nRectangles' Areas:")
print("Index\tLength\tWidth\tArea")
for i in range(num_rectangles):
    print(f"{i + 1}\t{lengths[i]}\t{widths[i]}\t{areas[i]}")
