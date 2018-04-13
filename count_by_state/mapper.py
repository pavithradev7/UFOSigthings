import datetime

input = open("complete.csv", "r")
output = open("Output.txt","w")

#initialize the state
state = 0
#reading all of the lines of the given input file
for line in input:

    # spliting of the csv file into a list of data
    listdata = line.strip().split(",")
   
    # verify that each line of the data in form of list is 11 
    if (len(listdata) == 11):
        # assign values to all attributes from data
        date_time, city, state, country, shape, durationInSeconds, durationInHourMin, comment, date_posted, latitude, longitude = listdata
        print(state)
        #Write into the file 
        output.write(str(state) + ",1\n")

            
# close the files
input.close()
output.close()