import re

with open(r"C:\Users\nrror\Desktop\Advent of Code\day_3.txt", 'r') as file:
    input = file.read()

def evaluate_instructions(memory):
    total = 0
    mul_enabled = True
    pattern = r"\bdon't\(\)|\bdo\(\)|\bmul\((\d{1,3}),(\d{1,3})\)"
    
    for match in re.finditer(pattern, memory):
        if match.group() == "do()":
            mul_enabled = True
        elif match.group() == "don't()":
            mul_enabled = False
        else:  # This must be a valid mul(X,Y)
            if mul_enabled:
                x = int(match.group(1))
                y = int(match.group(2))
                total += x * y
                
    return total

print(evaluate_instructions(input))
