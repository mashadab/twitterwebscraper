# Author: Mohammad Afzal Shadab (mashadab@utexas.edu)
# Date:   06/15/2020

#Source codes of Get Old Tweets for Python 3: 1. https://github.com/Jefferson-Henrique/GetOldTweets-python
#                                              2. https://pypi.org/project/GetOldTweets3/
#Please go to the above sites to read the instruction manual by which you can... 
# ... do a lot more i.e. controlling the Max Tweets, Saving Tweets, etc..

import GetOldTweets3 as got       #this library doesn't require access token and has no official twitter time limit (7 days)
import datetime as dt             #for time stamping
import matplotlib.pyplot as plt   #for plotting
import matplotlib.dates as mdates #for conversion of dates to required format
import time                       #for sleeping, if the HTTP requests are above the limit
import csv                        #for saving as an csv file

#Comment the lines bounded by pound (#) if your code has exceeded the limit of HTTP requests ...
# ... "Error 429: Too Many Requests" to continue from the same step
###################################################
QueryWord = "BlackLivesMatter"
#Start date
StartDay = 1
StartMonth = 5
StartYear  = 2020

#Can get rid of month and 
Location  = "Minnesota"
Radius    = "200mi" #200 miles radius from Minnesota

DaysGap   = 1        #day increment
Steps     = 43       #number of steps taken

#Date conversion to required format
Datetime = dt.datetime(StartYear,StartMonth,StartDay)
DateIterStart = str(Datetime.year) +"-" + str(Datetime.month) + "-" + str(Datetime.day)
Datetime = dt.datetime(StartYear,StartMonth,StartDay) + dt.timedelta(days=DaysGap)
DateIterEnd = str(Datetime.year) +"-" + str(Datetime.month) + "-" + str(Datetime.day)

#initialization
step = 0
NTweets  = [0 for row in range(Steps)]
DayEnd = [0 for row in range(Steps)]
##################################################

#time loop
while (step < Steps):
    
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(QueryWord).setNear(Location).setWithin(Radius).setSince(DateIterStart).setUntil(DateIterEnd)
    #tweetCriteria = got.manager.TweetCriteria().setQuerySearch(QueryWord).setSince(DateIterStart).setUntil(DateIterEnd)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets:
        if QueryWord not in tweet.text:   
            tweets.remove(tweet)
    
    #for tweet in tweets:
    #    print(tweet.text + '\n')
    
    NTweets[step] = len(tweets) 
    DayEnd[step]= Datetime  #it is actually end of the week
    print(f"The word '{QueryWord}' has been used in tweets", NTweets[step], " times during the days ", DateIterStart, "until", DateIterEnd) 

    step = step + 1
    
    #Date conversion to required format for next iteration
    Datetime = Datetime + dt.timedelta(seconds=1) 
    DateIterStart = str(Datetime.year) +"-" + str(Datetime.month) + "-" + str(Datetime.day)
    Datetime = Datetime + dt.timedelta(days=DaysGap)
    DateIterEnd = str(Datetime.year) +"-" + str(Datetime.month) + "-" + str(Datetime.day)
    time.sleep(1) #sleep for one second to reduce the rate limit

StepNo = [i+1 for i in range(Steps)]

#writing to csv file
with open(f'BLM_{Location}.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(StepNo)
    csv_writer.writerow(DayEnd)
    csv_writer.writerow(NTweets)

#plotting   
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(StepNo[:Steps],NTweets[:Steps],'k--')
plt.plot(StepNo[:Steps],NTweets[:Steps],'ro')
plt.axvline(StepNo[24], color='k', linestyle='solid',label='George Floyd\'s Murder')      #Murder of George Floyd, May 25, 2020
plt.axvline(StepNo[31], color='r', linestyle='solid',label='Lafayette Square incident')   #Lafayette Square Incident of June 1, 2020

#plt.gcf().autofmt_xdate()
plt.ylabel(f'# tweets')
plt.xlabel('Days')
#plt.ylim([0, 700])
plt.legend(loc='best', shadow=False, fontsize='x-large')
#plt.xlim(DayEnd[0], DayEnd[Steps-1])
#plt.locator_params(numticks=12)

StartDatetime = dt.datetime(StartYear,StartMonth,StartDay)
StartDatetime = str(StartDatetime.day) + "-" + str(StartDatetime.month)+ "-" + str(StartDatetime.year) 

plt.title(f'{Location} from {StartDatetime}')
plt.savefig(f'BLM_05012020_{Location}.png',bbox_inches='tight', dpi = 600)