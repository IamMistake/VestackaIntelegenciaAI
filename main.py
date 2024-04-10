input_string = "3,2,1;;"

# Split the input string into individual parts using ';;' as the separator
parts = input_string.split(';')

# Convert each part into a tuple
tuples_list = tuple(map(int, parts.split(',')))

print(tuples_list)
