import datetime

input = open("complete.csv", "r")
fout = open("MattMapperOutput.txt","w")

year = 0
for line in input:
    datalist = line.strip().split(",")
    if (len(datalist) == 11):
        date_time, city, state, country, shape, durationInSeconds, durationInHourMin, comment, date_posted, latitude, longitude = datalist
        if date_time != "":
            try:
                dt = datetime.datetime.strptime(date_time, '%m/%d/%Y %H:%M')
                print dt.year
                year = dt.year  
            except: 
                print "error" # only prints to console and only happens when the formatting is not correct
            fout.write(str(year) + ",1\n")

            
            

input.close()
fout.close()