with open(r"C:\Users\nrror\Desktop\Advent of Code\day_5_rules.txt", 'r') as rule_file:
    rule_input = rule_file.read().split()

with open(r"C:\Users\nrror\Desktop\Advent of Code\day_5_page_numbers.txt", 'r') as page_file:
    page_input = page_file.read().split()

new_list = []
for digit in rule_input:
    for number in digit.split():
        new_list.append(number)

paired_values = [item.split("|") for item in new_list]

rule_list = [[int(float(j)) for j in i] for i in paired_values]

page_strings = [item.split(",") for item in page_input]

page_list = [[int(float(j)) for j in i] for i in page_strings]

x_index = []
y_index = []
count = 0

for sublist in rule_list:
    x = sublist[0]
    y = sublist[1]
    print(x)
    print(y)
    for sublist2 in page_list:
        if (x in sublist2) and (y in sublist2):
            x_index = sublist2.index(x)
            y_index = sublist2.index(y)
            

#print(rule_list)
#print(page_list)