import pandas

# load csv file data.csv into pandas and display the structure
df = pandas.read_csv("data.csv")
# load just the first 10 lines of the csv file and print the data in the console
# print(df.iloc[0:500])
# print(df.columns)
# print(df.head)

# # Calculate the average KWH/hh for each LCLid
average_kwh_per_lclid = df.groupby("LCLid")["KWH/hh (per half hour) "].mean()

# Print the result
print("Avg KWH/hh per LCLid:", average_kwh_per_lclid)
# import pandas as pd

# # Load the csv file into a pandas dataframe
# df = pd.read_csv("data.csv")

# # Count the number of rows with a value of zero in the KWH/hh column
# num_zero_rows = len(df[df["KWH/hh"] == 0])

# # Print the result
# print(num_zero_rows)
