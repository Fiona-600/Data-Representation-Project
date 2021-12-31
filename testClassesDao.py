from ClassesDao import classesDao

Class1 = {
    "ID": "ABM1",
    "Class_Name": "Agility - Beginners",
    "Day": "Monday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Ciara"
}

Class2 = {
    "ID": "AIM1",
    "Class_Name": "Agility - Improvers",
    "Day": "Monday",
    "Time": "8pm",
    "Max_Participants": 10,
    "Trainer": "Jane"
}

Class3 = {
    "ID": "BOT1",
    "Class_Name": "Beginners - Obedience",
    "Day": "Tuesday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Joe"
}

Class4 = {
    "ID": "BOT2",
    "Class_Name": "Beginners - Obedience",
    "Day": "Tuesday",
    "Time": "8pm",
    "Max_Participants": 10,
    "Trainer": "Joe"
}

Class5 = {
    "ID": "ACW1",
    "Class_Name": "Agility Club",
    "Day": "Wednesday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Jane"
}

Class6 = {
    "ID": "IOT1",
    "Class_Name": "Improvers - Obedience",
    "Day": "Thursday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Dave"
}

Class7 = {
    "ID": "IOT2",
    "Class_Name": "Improvers - Obedience",
    "Day": "Thursday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Dave"
}

#returnValue = classesDao.create(Classes) #test - code for server.py
returnValue = classesDao.getAll()
print(returnValue)
returnValue = classesDao.findById(Class7['ID'])
print(returnValue)
returnValue = classesDao.update(Class7)
print(returnValue)
returnValue = classesDao.findById(Class7['ID'])
print(returnValue)
returnValue = classesDao.delete(Class7['ID'])
print(returnValue)
returnValue = classesDao.getAll()
print(returnValue)
