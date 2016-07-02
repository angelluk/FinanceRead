from matplotlib import pyplot as plt
from collections import Counter
# -*- coding: utf-8 -*-
"""
PLOT

"""

'''
    LINE CHART
'''


years = [1950,1960,1970,1980,1990,2000,2010]

gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years,gdp,color = 'blue', marker = 'o', linestyle = 'solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.xlabel("Years")

plt.show()


'''
    BAR CHART
'''
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West side story"]

num_oscars = [5,11,3,8,10]

xs = [i  for i, _ in enumerate(movies)] # define x shift for each movie

plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title('My favorite movies')

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies) # label on center of bar

plt.show()


'''
    ANOTHER BAR CHART
'''
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

decile = lambda grade: grade // 10 * 10  # round

histogram = Counter(decile(grade) for grade in grades) # how offen is appear each value of grades

plt.bar([x - 4 for x in histogram.keys()], # shift x on 4 left
        histogram.values(),                # height is probability
        8 )                                # default width

plt.axis([-5,105,0,5])      # range of x and y axis

plt.xticks([10 * i for i in range(11)])

plt.xlabel('Decile')
plt.ylabel(' 3 of students')
plt.title('Distribution of Exam 1 Grades')

plt.show()


'''
    LINE TRENDS
'''
variance = [1,2,4,8,16,32,64,128,256]

bias_squared = [256,128,64,32,16,8,4,2,1]

total_error = [ x + y for x,y in zip(variance,bias_squared)]

xs = [i for i , _ in enumerate(variance)]

plt.plot(xs,variance, 'g-', label='variance')
plt.plot(xs,bias_squared, 'r-.', label='bias^2')
plt.plot(xs,total_error, 'b:', label='total error')

plt.legend(loc=9) # top center position for legend
plt.xlabel('model complexity')
plt.title('The Bias - Variance Tradeoff')

plt.show()

'''
    SCATTERPLOTS
'''

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes)

# labels for each point

for label, friend_count, minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
                 xy=(friend_count,minute_count),
                 xytext=(5,-5),
                 textcoords='offset points')

plt.title('Daily Minutes vs. Number of Friends')
plt.xlabel('# of friend')
plt.ylabel('daily minte spent on the site')

plt.show()
