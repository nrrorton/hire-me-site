with open(r"C:\Users\nrror\Desktop\Advent of Code\day_5_rules.txt", 'r') as rule_file:
    rule_input = rule_file.read().split()

with open(r"C:\Users\nrror\Desktop\Advent of Code\day_5_page_numbers.txt", 'r') as rule_file:
    page_input = rule_file.read().split()

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

for page in page_list:
    flag = False
    for rule in rule_list:
        x = rule[0]
        y = rule[1]
        if (x in page) and (y in page):
            x_index = page.index(x)
            y_index = page.index(y)
            if x_index > y_index:
                flag = True
    if flag == False:
        middle_index = len(page) // 2
        count += page[middle_index]

print(count)




