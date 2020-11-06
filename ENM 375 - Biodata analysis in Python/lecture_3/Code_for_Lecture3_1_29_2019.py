#Ensure you are in the right directory
cd /Users/jennifercremins/Desktop/Teach_Spring2019/ENM375_Spring2018/Lecture3_slidesandcode_JEPC/


#Import required packages for plotting and descriptive statistics

import numpy as np
import matplotlib.pyplot as pyplot

#First, let's do some simple excercises
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

#% - remainder of the division of left operand by the right

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print 3 + 2 + 1 - 5 + 4 % 2 - float(1) / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

#Data Structures - Lists

#List

empt = []
empt 
type(empt)
empt2 = list()
three_lst = [1, 2, 3]
print(three_lst)
nested_lst = [[1, 2], [3, 4]]
print(nested_lst)
mult_types = [1, 'a', [True, None]]
print(mult_types)
from_range = list(range(3))
print(from_range)
big_lst = from_range + from_range
print(big_lst)

#indexing into a list

li = ['abc', 34, 4.34, 23]
print(li[1]), "Second item in the list."
print(li[0]), "First item in the list."
print(li[1:3]), "Second and Third item in the list."
print(li[-1]), "Last item in the list."

# Example: Rotten Tomatoes vs. the People

r1= ["Movie","Rotten Tomatoes","People"]
print(r1)
print(r1[0])
print(r1[1])
print(r1[2])
    

###### Plotting exercises


#Make your data structures. In this case, I use lists:
header = []
data = []

#Open your data file
input = open("20150901_Airplane.csv", 'rU')

#Loop through your data file line by line, clean up the lines, and then append them to lists
for line in input:
#print line
    if line.startswith('#'):
        print line
        header = line.strip('\n').split(',')
    else:
        #print line
        line = line.strip('\n').split(',')
        data.append(line)

input.close()

#Examine your new data structure
print data
print header, "here are the categories of each column"
print len(data)

#Now, start parsing your data to get the information you need for plotting and descriptive statistics

# Start by computing descriptive statistics on the number of flights per year across all cities for AirTran 

airtran_flights_number = []

for entry in data:
    #print entry
    #print entry[0]
    if entry[0] == 'AirTran':
        airtran_flights_number.append(int(entry[5]))

#Now, print the filled in list you have created:
print airtran_flights_number

average_flight_number = sum(airtran_flights_number)/(len(airtran_flights_number))


print average_flight_number, "here is the average number of flights per year for AirTran"

# Descriptive statistics - mean, pop variance, sample variance, median    
print np.mean(airtran_flights_number), "sample mean"
print np.var(airtran_flights_number), "population variance"
print np.var(airtran_flights_number,ddof = 1), "sample variance"
print np.median(airtran_flights_number), "median"
print np.std(airtran_flights_number,ddof = 1), "sample standard deviation"
sd = np.std(airtran_flights_number,ddof=1)
m = np.mean(airtran_flights_number)

#Let's start our plotting adventures on this data!

#Histogram - view the data in a frequency distribution - then change number of bins
pyplot.figure()
pyplot.hist(airtran_flights_number,20)
pyplot.xlabel('Number of flights across cities in the U.S.')
pyplot.ylabel('Frequency')
pyplot.title('AirTran Flight Distribution')
pyplot.show()

#Histogram - view the data in a relative frequency distribution
pyplot.figure()
pyplot.hist(airtran_flights_number,20,normed=True)
pyplot.xlabel('Number of flights across cities in the U.S.')
pyplot.ylabel('Relative Frequency')
pyplot.title('AirTran Flight Distribution')
pyplot.show()

# Now stratify the data to make a scatterplot of Flights on time vs. Flights delayed
airtran_flights_OT = []
airtran_flights_D = []

for entry in data:
    #print entry
    #print entry[0]
    if entry[0] == 'AirTran':
        airtran_flights_OT.append(int(entry[9]))
        airtran_flights_D.append(int(entry[6]))

#Scatterplot
pyplot.scatter(airtran_flights_OT, airtran_flights_D)
pyplot.xlabel('Flights On Time')
pyplot.ylabel('Flights Delayed')
pyplot.xlim(0, 2500)
pyplot.ylim(0,2500)
pyplot.show()

#Scatterplot
pyplot.scatter(airtran_flights_OT, airtran_flights_D)
pyplot.xlabel('Flights On Time')
pyplot.ylabel('Flights Delayed')
pyplot.xlim(0,400)
pyplot.ylim(0,100)
pyplot.show()

#Boxplot
combine = [airtran_flights_OT, airtran_flights_D]
pyplot.boxplot(combine)
pyplot.xticks(range(1,3,1), ['ON TIME', 'DELAYED'])
pyplot.ylabel('Number of flights')
pyplot.show()

*******Now, in class exercise: Make a strip chart of the AirTran flights OT vs. AirTran flights Delayed

#Strip Chart
x_OT = [1] * len(airtran_flights_OT)
x_D = [3] * len(airtran_flights_D)  
pyplot.plot(x_OT, airtran_flights_OT, marker = 'o', linestyle = 'None')
pyplot.plot(x_D, airtran_flights_D, marker = 'o', linestyle = 'None')
pyplot.xlim(0,4)
pyplot.xticks(range(1,4,2), ['ON TIME', 'DELAYED']) # Set some labels
pyplot.ylabel('Number of Flights')
pyplot.show()

