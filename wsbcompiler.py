#remember, "pip install praw"
import praw
import os
from datetime import datetime

#Authorises access to api
reddit = praw.Reddit(
    client_id=os.getenv('CLIENTID'),
    client_secret=os.getenv('CLIENTSECRET'),
    user_agent=os.getenv('USERAGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
    )

#Input a string, determine if it is true or false
def yesNo(input):
    if(input == "y"):
        return True
    if(input == "n"):
        return False

#Initializes config variables
subreddit = ""
sortType = ""
includeTitles = ""
includePosts = ""

#Checks if an automation .txt is being used
if(os.path.isfile("automation.txt")):
    #Checks length, then closes file
    automation = open("automation.txt", "r")
    lineAmount = len(automation.readlines())
    automation.close()

    automation = open("automation.txt", "r")


    i = 0
    while(i < lineAmount):
        line = automation.readline()
        splitLine = line.split(":")
        value = splitLine[1]
        if(i == 0):
            subreddit = value
        elif(i == 1):
            sortType = value
        elif(i == 2):
            includeTitles = yesNo(value)
        elif(i == 3):
            includePosts = yesNo(value)
        i += 1
    print("Automation script loaded")


#If automation .txt doesn't exist, manually asks question
#Stores information for what is being collected
if(os.path.isfile("automation.txt") == False):
    subreddit = str(input("What subreddit?: "))
    sortType = str(input("What sorting method?: "))
    includeTitles = bool(yesNo(input("Include titles?: (y/n): ")))
    includePosts = bool(yesNo(input("Include post bodys?: (y/n): ")))

print(subreddit)
print(sortType)
print(includeTitles)
print(includePosts)

input("Press enter to continue")


dateTimeVar = datetime.utcnow()
date = dateTimeVar.strftime("%d/%m/%Y")
time = dateTimeVar.strftime("%H:%M:%S")

#for submission in reddit.subreddit(subreddit).sortType(limit=10):
#    submission.title()
