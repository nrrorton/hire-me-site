with open(r"C:\Users\nrror\Desktop\Advent of Code\day_6_test_map_input.txt", 'r') as file:
    test_input = file.read().split('\n')

for row in test_input:
    for col in test_input:
        print()
    print(row)

#input = test_input.replace(',', '')

"""for char in input:
    if char == '#':
        hash_locations = input.index('#')
        print(hash_locations)
    if char == '^':
        carrot_location = input.index('^')
        print(carrot_location)"""
