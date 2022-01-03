import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
)

cursor = db.cursor()

# CREATE METHODS:
# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS ClassTimetable")
cursor.execute("USE ClassTimetable")

#Delete Classes table
cursor.execute("DROP TABLE Classes")

# Create the table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Classes(Class_ID varchar(20) PRIMARY KEY,Class_Name varchar(50),Day varchar(50),Time varchar(50), Max_Participants int,Trainer varchar(50))")
#cursor.execute("CREATE TABLE IF NOT EXISTS Classes(Class_Name varchar(100),Day varchar(10),Time varchar(10),Max_Participants int)")
#cursor.execute("CREATE TABLE Classes(Class_Name varchar(100),Day varchar(10),Time varchar(10),Max_Participants int)")


#UPDATE METHODS:

#Add a New Class:
sql = "INSERT INTO Classes values(%s,%s,%s,%s,%s,%s)"
#values = ("Agility - Beginners", "Monday","7pm","10"), ("Agility - Improvers", "Monday","8pm","10"), ("Beginners - Obedience", "Tuesday","8pm","10"), ("Agility Club", "Wednesday","7pm","10"), ("Improvers - Obedience", "Thursday","7pm","10")
values = ("ABM1","Agility - Beginners", "Monday","7pm",10,"Ciara"), ("AIM1","Agility - Improvers", "Monday","8pm",10,"Jane"), ("BOTU1","Beginners - Obedience", "Tuesday","7pm",10,"Joe"), ("BOTU2","Beginners - Obedience", "Tuesday","8pm",10,"Joe"), ("ACW1","Agility Club", "Wednesday","7pm",10,"Jane"), ("IOTH1","Improvers - Obedience", "Thursday","7pm",10,"Dave"), ("IOTH2","Improvers - Obedience", "Thursday","8pm",10,"Dave")

cursor.executemany(sql,values)

#Change Class Type:
#sql="UPDATE Classes SET ID = %s, Class_Name = %s, Day=%s, Time=%s, Max_participants=%s, Trainer=%s where ID = %s"
#values = ("BOM1","Beginners - Obedience", "Monday","7pm",10,"Joe","ABM1")
#cursor.execute(sql,values)

#Change Trainer:
#sql="UPDATE Classes SET ID = %s, Class_Name = %s, Day=%s, Time=%s, Max_participants=%s, Trainer=%s where ID = %s"
#values = ("AIM1","Agility - Improvers", "Monday","8pm",10,"Jim","AIM1")
#cursor.execute(sql,values)

db.commit()

