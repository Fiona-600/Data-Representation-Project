from ClassesDao import classesDao

Class1 = {
    "Class_ID": "ABM1",
    "Class_Name": "Agility - Beginners",
    "Day": "Monday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Ciara"
}

Class2 = {
    "Class_ID": "AIM1",
    "Class_Name": "Agility - Improvers",
    "Day": "Monday",
    "Time": "8pm",
    "Max_Participants": 10,
    "Trainer": "Jane"
}

Class3 = {
    "Class_ID": "BOTU1",
    "Class_Name": "Beginners - Obedience",
    "Day": "Tuesday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Joe"
}

Class4 = {
    "Class_ID": "BOTU2",
    "Class_Name": "Beginners - Obedience",
    "Day": "Tuesday",
    "Time": "8pm",
    "Max_Participants": 10,
    "Trainer": "Joe"
}

Class5 = {
    "Class_ID": "ACW1",
    "Class_Name": "Agility Club",
    "Day": "Wednesday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Jane"
}

Class6 = {
    "Class_ID": "IOTH1",
    "Class_Name": "Improvers - Obedience",
    "Day": "Thursday",
    "Time": "7pm",
    "Max_Participants": 10,
    "Trainer": "Dave"
}

Class7 = {
    "Class_ID": "IOTH2",
    "Class_Name": "Improvers - Obedience",
    "Day": "Thursday",
    "Time": "8pm",
    "Max_Participants": 10,
    "Trainer": "Dave"
}

#returnValue = classesDao.create(Classes) #test - code for server.py
returnValue = classesDao.getAll()
print(returnValue)
returnValue = classesDao.findById(Class7['Class_ID'])
print(returnValue)
returnValue = classesDao.update(Class7)
print(returnValue)
returnValue = classesDao.findById(Class7['Class_ID'])
print(returnValue)
returnValue = classesDao.delete(Class7['Class_ID'])
print(returnValue)
returnValue = classesDao.getAll()
print(returnValue)
