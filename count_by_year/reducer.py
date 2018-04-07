input = open("mattsorteddata.txt", "r")
output = open("mattresults.txt","w")

key = ""
value = 0

for line in input:
    datalist = line.strip().split(",")
    if len(datalist) == 2:
        year, count = datalist
    if year != key:
        output.write(key + ", " + str(value) + "\n")
        key = year
        value = 0
    value = value + 1

output.write(key + ", " + str(value) + "\n") 

input.close()
output.close()