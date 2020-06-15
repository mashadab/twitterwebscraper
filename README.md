# twitterwebscraper
Python based Twitter Webscrapper with no official time limit 

Salient features:
Program currently -
  1. Calculates and can also print Tweets with a "keyword" for a specific period in a specific region
  2. Sleeps to avoid 'Error 429: Too Many Requests'
  3. Bypasses Twitter official time limit of 7 days
  4. Plots the results using Matplotlib.pyplot
  5. Saves the file as csv

Program can also -
  1. Control the maximum number of tweets
  2. Constrains to a specific twitter profile
  and a lot more. Please refer to Source codes of Get Old Tweets for Python 3: 
## > https://github.com/Jefferson-Henrique/GetOldTweets-python
## > https://pypi.org/project/GetOldTweets3/
  
## Libraries used   
GetOldTweets3     #this library doesn't require Twitter official access token and has no official twitter time limit (7 days)

datetime          #for time stamping

matplotlib.pyplot #for plotting

matplotlib.dates  #for conversion of dates to required format

time              #for sleeping, if the HTTP requests are above the limit

csv               #for saving as csv file

## Comments are given in the code
