with open("data.csv", "r") as input_file, open("exceptions.txt", "w") as exceptions:
    column_names = input_file.readline()
    print("Column names: ", column_names)

    first_line = input_file.readline()
    current_LDLid = first_line.split(",")[0]
    try:
        current_KWH = float(first_line.split(",")[-1])
    except ValueError:
        print("Exception: ", first_line)
        exceptions.write(first_line)
    print(current_LDLid, " KWH: ", current_KWH, type(current_KWH))

    for index in range(30):
        print("First line: ", first_line)

        zero_count = 0
        if current_KWH == 0:
            zero_count += 1

        with open(f"data/{current_LDLid}.csv", "w") as output_file:
            output_file.write(column_names)
            output_file.write(first_line)
            new_line = input_file.readline()
            new_LDLid = new_line.split(",")[0]
            try:
                current_KWH = float(first_line.split(",")[-1])
            except ValueError:
                print("Exception: ", first_line)
                exceptions.write(first_line)

            # new_KWH = float(new_line.split(",")[-1])
            print(new_LDLid, " KWH: ", new_KWH, type(new_KWH))

            if new_KWH == 0:
                zero_count += 1

            while new_LDLid == current_LDLid:
                output_file.write(new_line)
                new_line = input_file.readline()
                new_LDLid = new_line.split(",")[0]
                print("New LIne: ", new_line)
                new_KWH = float(new_line.split(",")[-1])
                print(new_LDLid, " KWH: ", new_KWH, type(new_KWH))
                if new_KWH == 0:
                    zero_count += 1
                if zero_count > 0 and new_LDLid != current_LDLid:
                    exceptions.write(f"LDL: {current_LDLid}, Zeros: {zero_count}")
                    if new_KWH == 0:
                        zero_count = 1
                    else:
                        zero_count = 0

            first_line = new_line
            current_LDLid = new_LDLid
            current_KWH = new_KWH
            continue
