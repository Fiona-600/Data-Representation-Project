import mysql.connector
from mysql.connector import cursor
#from .models import ConfigFile
#import dbconfig as cfg

class ClassesDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'root',
            database ='classtimetable'
        )
        #print ("connection made")

    def create(self, Classes):
        cursor = self.db.cursor()
        sql = "insert into Classes (Class_ID, Class_Name, Day, Time, Max_Participants,Trainer) values (%s,%s,%s,%s,%s,%s)"
        values = [
            Classes["Class_ID"],
            Classes["Class_Name"],
            Classes["Day"],
            Classes["Time"],
            Classes["Max_Participants"],
            Classes["Trainer"]
            ]
        
        cursor.execute(sql, values)
        self.db.commit()
        #print("create:")
        #return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from Classes order by Day,Time'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, Class_ID):
        cursor = self.db.cursor()
        sql = 'select * from Classes where Class_ID = %s'
        values = [Class_ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        #print("\nfindByID:")
        return self.convertToDict(result)
        

    def update(self, Classes):
        cursor = self.db.cursor()
        sql = "UPDATE Classes SET Class_Name = %s, Day=%s, Time=%s, Max_participants=%s, Trainer=%s where Class_ID = %s"
        values = [
            #Classes['Class_ID'],
            Classes["Class_Name"],
            Classes["Day"],
            Classes["Time"],
            Classes["Max_Participants"],
            Classes["Trainer"],
            Classes["Class_ID"],
            ]

        cursor.execute(sql, values)
        self.db.commit()
        return Classes


    def delete(self, Class_ID):
       cursor = self.db.cursor()
       sql = "DELETE FROM Classes WHERE Class_ID = %s"
       values = [Class_ID]
       cursor.execute(sql, values)
       self.db.commit()
       return {}



    def convertToDict(self, result):
        colnames = ["Class_ID", "Class_Name", "Day", "Time", "Max_participants", "Trainer"]
        Classes = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                Classes[colName] = value
        #self.db.commit()
        return Classes

classesDao = ClassesDao()
