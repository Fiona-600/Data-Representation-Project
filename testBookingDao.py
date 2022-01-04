from BookingDao import bookingDao

Booking1 = {
    "Dog_Name": "Elmo",
    "Class_ID": "ABM1",
    "Class_Name": "Agility - Beginners",
    "Day": "Monday",
    "Time": "7pm"
}

Booking2 = {
    "Dog_Name": "Thor",
    "Class_ID": "AIM1",
    "Class_Name": "Agility - Improvers",
    "Day": "Monday",
    "Time": "7pm"
}

returnValue = bookingDao.create(Booking1) #test - code for server.py
returnValue = bookingDao.create(Booking2) #test - code for server.py
returnValue = bookingDao.getAll()
print(returnValue)
returnValue = bookingDao.findById(Booking1['Dog_Name'])
print(returnValue)
returnValue = bookingDao.update(Booking2)
print(returnValue)
returnValue = bookingDao.getAll()
print(returnValue)
returnValue = bookingDao.delete(Booking1['Dog_Name'])
print(returnValue)
returnValue = bookingDao.getAll()
print(returnValue)
