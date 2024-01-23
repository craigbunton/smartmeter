with open("data.csv", "r") as input_file:
    # count12 = 0
    countNul = 0
    line_num = 0
    while line_num < 10000000:
        line = input_file.readline()
        # if "12:37" in line:
        #     print("12:37 : ", line)
        #     count12 += 1
        if "Null" in line:
            print("Nul : ", line)
            countNul += 1
        line_num += 1
