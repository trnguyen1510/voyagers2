import pymongo
from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://Voyagers:Voyagers123@cluster0.zshph.mongodb.net/<dbname>?retryWrites=true&w=majority")
mydb = myclient["voyagers"]
mycol = mydb["survey_survey"]
try:
    mycol.insert_one({'country': "ertrete"})
    print("done")
except:
    print("not working")

