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
                #print dt.year
                year = dt.year
                fout.write(year + ",1\n")
                
            except: 
                print "error"
            
            

input.close()
fout.close()