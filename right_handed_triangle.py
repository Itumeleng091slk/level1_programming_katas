
def triangle(num_rows):
    for row_count in range(num_rows + 1):
        print("#" * row_count)

# Alternate solution
"""def triangle(num_rows):
    row_count = 0
    while(row_count <= num_rows):
        print("#" * row_count)
        row_count = row_count + 1
"""
row_number = int(input("Enter your triangle number: "))
triangle(row_number)
