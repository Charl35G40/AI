#Imports
from string import punctuation
import twitter
import re
import sys
import pickle

try:
	print("Analyzing: '" + sys.argv[1] + "'")
except:
	sys.argv.append("Donald Trump")
	print("Analyzing: '" + sys.argv[1] + "'")


searchWord = sys.argv[1]

#Twitter
anondev = twitter.Api(consumer_key = 'ts8P8m9DhKBX5PJEu4oKdfKbq',
                    consumer_secret = 'oXLRIBS9ajWxJQRUvfVvwojpKQAi3RjiA3SGHk4SR910nqsFj8',
                    access_token_key = '837375139490627584-aDq9sWh4QMCWijG3NC5ug7yfCFXOlSh',
                    access_token_secret = '6WjI86zsyzirhev3uMC4N5yJJMAyCK8DEpzJ6QcFcUWS9')

testAPI = twitter.Api()

def GetStatuses():
	stsList = anondev.GetSearch(term=searchWord)
	lastID = stsList[-1].id - 1
	#stsFile = pickle.load(open('Statuses.pkl', 'r+b'))
	r = 67
	x = 0
	#print(stsFile)
	for i in range(r):
		stsList.extend(anondev.GetSearch(term=searchWord, max_id=lastID))
		lastID = stsList[-1].id - 1
	#pickle.dump(stsList, open('Statuses.pkl', 'w+b'))
	return stsList
 
stsAll = GetStatuses()
print(stsAll)
print(len(stsAll))
print(sys.argv[0])
print(sys.argv[1])
