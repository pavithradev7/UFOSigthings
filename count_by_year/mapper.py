import datetime

input = open("complete.csv", "r")
fout = open("MattMapperOutput.txt","w")

#initialize the year var to 0
year = 0
#read through all of the lines of the input file
for line in input:
    # split the csv file into a data list
    datalist = line.strip().split(",")
    # verify that each line of the datalist is 11 so we know that there isn't any additional columns or weird errors
    if (len(datalist) == 11):
        # assign values to all of the things in the datalist
        date_time, city, state, country, shape, durationInSeconds, durationInHourMin, comment, date_posted, latitude, longitude = datalist
        # check for empty value
        if date_time != "":
            # try to see if we can get a good date read from the date_time section
            try:
                # if datetime is in the proper format we will parse it as a date so we can get the year from the date
                dt = datetime.datetime.strptime(date_time, '%m/%d/%Y %H:%M')
                # print it to the console
                print dt.year
                # assign it to the year to bring it out of the try block
                year = dt.year  
            except: 
                # indicate that there was an error
                print "error" # only prints to console and only happens when the formatting is not correct
            # write to the file.
            fout.write(str(year) + ",1\n")

            
# close the files
input.close()
fout.close()