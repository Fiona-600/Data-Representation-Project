import mysql.connector
from mysql.connector import cursor

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
        sql = "insert into Classes (ID, Class_Name, Day, Time, Max_Participants,Trainer) values (%s,%s,%s,%s,%s,%s)"
        values = [
            Classes["ID"],
            Classes["Class_Name"],
            Classes["Day"],
            Classes["Time"],
            Classes["Max_Participants"],
            Classes["Trainer"]
            ]
        
        cursor.execute(sql, values)
        self.db.commit()
        print("create:")
        return cursor.lastrowid

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

    def findById(self, ID):
        cursor = self.db.cursor()
        sql = 'select * from Classes where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        #print("\nfindByID:")
        return self.convertToDict(result)
        

    def update(self, Classes):
        cursor = self.db.cursor()
        sql = "UPDATE Classes SET Class_Name = %s, Day=%s, Time=%s, Max_participants=%s, Trainer=%s where ID = %s"
        values = [
            Classes["Class_Name"],
            Classes["Day"],
            Classes["Time"],
            Classes["Max_Participants"],
            Classes["Trainer"],
            Classes["ID"],
            ]

        cursor.execute(sql, values)
        self.db.commit()
        return Classes


    def delete(self, ID):
       cursor = self.db.cursor()
       sql = "DELETE FROM Classes WHERE ID = %s"
       values = [ID]
       cursor.execute(sql, values)
       return {}



    def convertToDict(self, result):
        colnames = ["ID", "Class_Name", "Day", "Time", "Max_participants", "Trainer"]
        Classes = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                Classes[colName] = value
        return Classes

classesDao = ClassesDao()
