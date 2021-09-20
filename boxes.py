# file name: boxes.py
# author: Amon Brollo

# Import the math module so that it can be used in this program.
import math

manufactured_items = int(input("Enter the number of items: "))
pack_per_box = int(input("Enter the number of items per box: "))

# Compute the number of boxes.
num_boxes = math.ceil(manufactured_items / pack_per_box)

# Display the results for the user to see.
print(f"For {manufactured_items} items, packing {pack_per_box} items in each box, you will need {num_boxes} boxes.")
