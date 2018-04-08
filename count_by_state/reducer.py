input = open("sorteddata.txt", "r")
output = open("results.txt","w")

# Have a key and initialize it 
key = ""
# initialize the current value
currvalue = 0
# read all of the lines from the given input file
for line in input:
     # split the lines 
    listdata = line.strip().split(",")
    # if there is 2 values in data go into it
    if len(listdata) == 2:
         # have two values embedded from data
        state, count = listdata
    # Checking if the current stae is equal to the key
    if state != key:
        # Write the value into the output file and later reset it.
        output.write(key + ", " + str(currvalue) + "\n")
        print key + ", " + str(currvalue) + "\n"
        key = state
        currvalue = 0
   # increase the current value by one to get the occurance of sightings for each state
    currvalue = currvalue + 1
#print(value)
# Again write it into file since the last line wont be written inside the loop
output.write(key + ", " + str(currvalue) + "\n") 
print key + ", " + str(currvalue) + "\n"
# close the file
input.close()
output.close()