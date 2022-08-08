# Opening and reading the file
with open("exemplo2.txt", "r") as file:
    operations = file.readlines()
    file.close()
    numberOfLines = len(operations)

# Reading the first line of the file and converting it to a int     
numberOfoperationsLine = operations[0]
numberOfoperations = int(numberOfoperationsLine)
operationsRange = numberOfoperations * 3

# Operations
def union():
    group1 = set(operations[index +1])
    group2 = set(operations[index +2])
    group3 = group1 | group2
    if "\n" in group3:
        group3.remove("\n")
    if "," in group3:
        group3.remove(",")
    if " " in group3:
        group3.remove(" ") 
    str(group3)
    print("Union operation result:", group3)

def intersection():
    group1 = set(operations[index +1])
    group2 = set(operations[index +2])
    group3 = group1 & group2
    if "\n" in group3:
        group3.remove("\n")
    if "," in group3:
        group3.remove(",")
    if " " in group3:
        group3.remove(" ") 
    str(group3)
    print("Intersection operation result:", group3)

def difference():
    group1 = set(operations[index +1])
    group2 = set(operations[index +2])
    group3 = group1 - group2
    if "\n" in group3:
        group3.remove("\n")
    if "," in group3:
        group3.remove(",")
    if " " in group3:
        group3.remove(" ") 
    str(group3)
    print("Difference operation result:", group3)

def cartesianProduct():
    group1 = set(operations[index +1])
    group2 = set(operations[index +2])
    group3 = group1 | group2
    if "\n" in group3:
        group3.remove("\n")
    if "," in group3:
        group3.remove(",")
    if " " in group3:
        group3.remove(" ") 
    str(group3)
    print("Cartesian Product result:", group3)


index = 0
if operationsRange <= numberOfLines:
    for index in range(operationsRange):
        if index <= operationsRange:
            if operations[index] == "U\n":
                union()
            elif operations[index] == "I\n":
                intersection()
            elif operations[index] == "D\n":
                difference()
            elif operations[index] == "C\n":
                cartesianProduct()
            else: print("") 
            operations.append(operations[index+1])
        else:
            print("out of range")
else:
    print("out of range")