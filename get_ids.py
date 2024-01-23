ids = set()
with open("data.csv", "r") as input_file:
    for line in input_file:
        if "LCLid" in line:
            continue
        else:
            a, b, c, d = line.split(",")
            ids.add(a)

with open("ids.txt", "w") as output_file:
    for i in sorted(list(ids)):
        output_file.write(i)
