# Trabalho 1 - Resolução de Problemas de Natureza Discreta
# Estudante: Luiz Henrique Baldão Filho

# Opening and reading the file
with open("exemplo1.txt", "r") as file:
    operations = file.readlines()
    file.close()
    numberOfLines = len(operations)

# Reading the first line of the file and converting it to a int
numberOfoperationsLine = operations[0]
numberOfoperations = int(numberOfoperationsLine)
operationsRange = numberOfoperations * 3

# Operations


def union():
    group1 = set(operations[index + 1])
    group2 = set(operations[index + 2])
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
    group1 = set(operations[index + 1])
    group2 = set(operations[index + 2])
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
    group1 = set(operations[index + 1])
    group2 = set(operations[index + 2])
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
    group1 = set(operations[index + 1])
    group2 = set(operations[index + 2])
    if "\n" in group1 & group2:
        group1.remove("\n"), group2.remove("\n")
    if "," in group1 & group2:
        group1.remove(","), group2.remove(",")
    if " " in group1 & group2:
        group1.remove(" "), group2.remove(" ")
    lines = [group1, group2]
    result = [[]]
    for line in lines:
        result = [x+[y] for x in result for y in line]

    print("Cartesian product operation result:", result)


# Executing the operations
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
            else:
                print("")
            operations.append(operations[index+1])
        else:
            print("out of range")
else:
    print("out of range")
