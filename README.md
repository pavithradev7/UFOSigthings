## README

## Project Name
	UFO Sightings from the Last Century
	44-564-01
	Project Group 1F
	Developers: Matthew Woolery, Pavithra Devdas
## Links
Repository: [https://bitbucket.org/mwoolery/ufo-sightings-from-the-last-century](https://bitbucket.org/mwoolery/ufo-sightings-from-the-last-century)

Issue Tracker: [https://bitbucket.org/mwoolery/ufo-sightings-from-the-last-century/issues?status=new&status=open](https://bitbucket.org/mwoolery/ufo-sightings-from-the-last-century/issues?status=new&status=open)

## Introduction
	Our project is an analysis of reported UFO sightings from the past century.  We would like to see count of the number of annually reported
	UFO Sightings so we can see if there has been an increase in sightings over the years or how sighting counts have changed after some famous 
	UFO events such as Roswell in the late 1930's.  We would also like to check the amount of sightings for each state, that way we can tell if 
	a certain state is more likely to report sightings, and because of this we could infer that we are more likely to sight one ourselves in one of
	these states.
## Data Source
	We found a source of data that is about 28MB in size which includes information about 89000 reported UFO Sightings. The fields included in this
	data source are datetime, city, state, country, shape, duration (seconds), duration(hours/min), comment, date posted, latitude, longitude.  It
	came in a CSV file and appears to be well structured data.
	Examples of values given are:
		datetime: 10/10/1949 20:30
		city: san marcos
		state: tx
		country: us
		shape: cylinder
		duration(seconds): 2700
		duration(hour/min): 45 minutes
		comment: This event took place in early fall around 1949-50...
		dateposted: 4/27/2004
		latitude: 29.8830556
		longitude: -97.9411111
	The dates and times go back to the early 1900's. The city, state, and country are given for a few different countries, we will primarily look at US cities.
	


## Data Source Link
[https://www.kaggle.com/NUFORC/ufo-sightings/data](https://www.kaggle.com/NUFORC/ufo-sightings/data)
## The Challenge (Big Data Qualifications)
	Volume: It is has around 89000 records, although this can be done with excel for the most part, it is still many records that we could not do buy hand easily but it will continue to grow
	Variety: A variety of calculations can be done, you could find occurences by location, figure out common shapes and descriptions, and find how the have changed in the past century
	Veracity: The data is mostly easy to go through, but if you wanted to analyze the comments given by each person, it could be challenging.
	Velocity: It is easy to tell that the amount of sightings have gone up rapidly, the beginning of the century only has a few reports, but later on there are thousands per year.
## Big Data Questions
	Matt's Question: Has the amount of sightings per year changed after famous UFO events such as Roswell has occured. I will be finding the count of sightings
					 by year and looking at famous UFO events to see if after their occurance caused some increase or decrease. An increase could signify that
					 it may just be people trying to report UFO's to be part of a bandwagon. No dramatic change could mean that sightings are just becoming more common
	
	Pavithra's Question: I will find the count of the number of reported UFO sightings for each U.S. state.
	
## Big Data Solutions
	Matt Big Data Solutions:
		Mapper input (CSV Formatted File):  10/13/1996 3:19	reno	nv	us	triangle	2400	40 min.	At 3:19 am&#44 bright light seen outside window and then one small tugboat triangular shaped aircraft seen over the house and then both oc	3/7/1998	39.5297222	-119.8127778
		Mapper output / Reducer input:  1940	1
		Reducer output:  1940	 159
		Language:  I will be using Python
		Chart: I will display a line graph, that way you can view how the values had increased or decreased by year. 
	Pavithra Big Data Solutions:
		Mapper input (CSV Formatted File): 10/10/1949 20:30	san marcos	tx	us	cylinder	2700	45 minutes	This event took place in early fall around 1949-50. It occurred after a Boy Scout meeting in the Baptist Church. The Baptist Church sit	4/27/2004	29.8830556	-97.9411111	
		Mapper output / Reducer input: tx 1
		Reducer output:tx 4394
		Language: I will be using Python
		Chart: I will display a bar graph, which shows what state has how many UFO sightings
