input = open("mattsorteddata.txt", "r")
output = open("mattresults.txt","w")

# initialize the key
key = ""
# initialize the value
value = 0
# read all of the lines from the input file
for line in input:
    # split the lines by the comma values
    datalist = line.strip().split(",")
    # if there is 2 categories a line it is right and we then go inside
    if len(datalist) == 2:
        # we make a data list with 2 categories
        year, count = datalist
    # if the year is not equal to the key
    if year != key:
        # we go in and write the value of the year and then move on to the next year and reset the value
        output.write(key + ", " + str(value) + "\n")
        print key + ", " + str(value) + "\n"
        key = year
        value = 0
    # increment the value
    value = value + 1
# write the value of the last item
output.write(key + ", " + str(value) + "\n") 
print key + ", " + str(value) + "\n"
# close the file
input.close()
output.close()