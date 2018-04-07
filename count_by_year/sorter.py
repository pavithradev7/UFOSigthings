input = open("MattMapperOutput.txt", "r")
output = open("mattsorteddata.txt","w")

data = input.readlines()
data.sort()

for line in data:
    datalist = line.strip().split(",")
    year, count = datalist
    output.write(year + ", " + count + "\n")

input.close()
output.close()