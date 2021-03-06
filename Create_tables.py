import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
)

cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS ClassTimetable")
cursor.execute("USE ClassTimetable")

#Delete Classes table - testing only to reset the database to original values
cursor.execute("DROP TABLE Classes")

# Create the 'Classes' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Classes(Class_ID varchar(20) PRIMARY KEY,Class_Name varchar(50),Day varchar(50),Time varchar(50), Max_Participants int,Trainer varchar(50))")

#Populate the 'CLasses' table of the initial database:
sql = "INSERT INTO Classes values(%s,%s,%s,%s,%s,%s)"
values = ("ABM1","Agility - Beginners", "Monday","7pm",10,"Ciara"), ("AIM1","Agility - Improvers", "Monday","8pm",10,"Jane"), ("BOTU1","Beginners - Obedience", "Tuesday","7pm",10,"Joe"), ("BOTU2","Beginners - Obedience", "Tuesday","8pm",10,"Joe"), ("ACW1","Agility Club", "Wednesday","7pm",10,"Jane"), ("IOTH1","Improvers - Obedience", "Thursday","7pm",10,"Dave"), ("IOTH2","Improvers - Obedience", "Thursday","8pm",10,"Dave")
cursor.executemany(sql,values)

# Create the 'Booking' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Booking(Dog_Name varchar(30) PRIMARY KEY,Class_ID varchar(10),Class_Name varchar(50),Day varchar(50),Time varchar(50))")

#Populate the 'Booking' table of the initial database
sql = "INSERT INTO Booking values(%s,%s,%s,%s,%s)"
values = ("Daisy","ABM1","Agility - Beginners", "Monday","7pm"), ("Rover","AIM1","Agility - Improvers", "Monday","8pm")
cursor.executemany(sql,values)

db.commit()

