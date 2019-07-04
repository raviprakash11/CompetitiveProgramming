'''Exercise 36 (and Solution)
This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.
In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.
If you are using a purely web-based interface for coding, this exercise won’t work for you, since it requires installing the bokeh Python package. Now might be a good time to install Python on your own computer.'''
import json
from collections import Counter

#function to read a json and returns a dictionary
def readJson(file):
    with open(file, "r") as f:
        print('Opening file ',file)
        return json.load(f)
#function to receive a dictionary and update the json file
def updateJson(file, diction):
    with open(file, "w") as f:
        json.dump(diction, f)
        print('File {} updated!'.format(file))

#storage json file in a dictionary
f = 'birthday.json'
mydict = readJson(f)


birthList = list(mydict.values())
newList = []

for birth in birthList:
    vector = birth.split('/')
    if int(vector[1]) == 1:
        newList.append('January')
    if int(vector[1]) == 2:
        newList.append('February')
    if int(vector[1]) == 3:
        newList.append('March')
    if int(vector[1]) == 4:
        newList.append('April')
    if int(vector[1]) == 5:
        newList.append('May')        
    if int(vector[1]) == 6:
        newList.append('June')
    if int(vector[1]) == 7:
        newList.append('July')
    if int(vector[1]) == 8:
        newList.append('August')        
    if int(vector[1]) == 9:
        newList.append('September')
    if int(vector[1]) == 10:
        newList.append('October')
    if int(vector[1]) == 11:
        newList.append('November')
    if int(vector[1]) == 12:
        newList.append('December')
    
c = dict(Counter(newList))

print(c)
print(list(c.keys()))
print(list(c.values()))

from bokeh.plotting import figure, show, output_file

# we specify an HTML file where the output will go
output_file("plot.html")

# load our x and y data
x_categories = list(c.keys())
x = list(c.keys())
y = list(c.values())

# create a figure
p = figure()
p = figure(x_range=x_categories)

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)
