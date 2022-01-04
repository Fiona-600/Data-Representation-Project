import mysql.connector
from mysql.connector import cursor

class BookingDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'root',
            database ='classtimetable'
        )

    def create(self, Booking):
        cursor = self.db.cursor()
        sql = "insert into Booking (Dog_Name, Class_ID, Class_Name, Day, Time) values (%s,%s,%s,%s,%s)"
        values = [
            Booking["Dog_Name"],
            Booking["Class_ID"],
            Booking["Class_Name"],
            Booking["Day"],
            Booking["Time"],
        ]
        
        cursor.execute(sql, values)
        self.db.commit()

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from Booking order by Class_ID'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, Dog_Name):
        cursor = self.db.cursor()
        sql = 'select * from Booking where Dog_Name = %s'
        values = [Dog_Name]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        #print("\nfindByID:")
        return self.convertToDict(result)
        

    def update(self, Booking):
        cursor = self.db.cursor()
        sql = "UPDATE Booking SET Class_ID = %s, Class_Name = %s, Day=%s, Time=%s where Dog_Name=%s"
        values = [
            Booking['Class_ID'],
            Booking["Class_Name"],
            Booking["Day"],
            Booking["Time"],
            Booking["Dog_Name"]
        ]

        cursor.execute(sql, values)
        self.db.commit()
        return Booking


    def delete(self, Dog_Name):
       cursor = self.db.cursor()
       sql = "DELETE FROM Booking WHERE Dog_Name = %s"
       values = [Dog_Name]
       cursor.execute(sql, values)
       self.db.commit()
       return {}

    def convertToDict(self, result):
        colnames = ["Dog_Name","Class_ID", "Class_Name", "Day", "Time"]
        Booking = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                Booking[colName] = value
        return Booking

bookingDao = BookingDao()
