input = open("Output.txt", "r")
output = open("sorteddata.txt","w")

# read all lines and put it in the data
datafile = input.readlines()
# Sorting the input based on state
datafile.sort()

# go through each line of data
for line in datafile:
    # split the data by the csv
    listdata = line.strip().split(",")
    # put the values into a list of data
    state, count = listdata
    print state + ", " + count + "\n"
      # write it out to a file with "," to separte the state and number of times state occurs
    output.write(state + ", " + count + "\n")

# close the files used
input.close()
output.close()