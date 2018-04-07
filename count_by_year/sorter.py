input = open("MattMapperOutput.txt", "r")
output = open("mattsorteddata.txt","w")

# get all of the lines and put it into data
data = input.readlines()
# sort it by the first field, in this case the date
data.sort()

# go through each line of data
for line in data:
    # split the data by the csv
    datalist = line.strip().split(",")
    # put the values into a datalist
    year, count = datalist
    # write it out to a file in the following format, it writes the sorted list this way
    output.write(year + ", " + count + "\n")

# close the files used
input.close()
output.close()