from flask import Flask, jsonify, request, abort
from BookingDao import bookingDao
import os
from flask import send_from_directory

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Add favicon:
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'staticpages'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Check Connection:
# Test:
# curl "http://127.0.0.1:5000" - test working
@app.route('/')
def index():
    return "hello"


# Return all Bookings:
# Test:
# curl "http://127.0.0.1:5000/Booking" - test working
@app.route('/Booking')
def getAll():
    #print("in getall")
    return jsonify(bookingDao.getAll())

# Get by ID:
#curl "http://127.0.0.1:5000/Booking/Daisy" - test working
@app.route('/Booking/<Dog_Name>')
def findById(Dog_Name):
    return jsonify(bookingDao.findById(Dog_Name))   


# Create new class:
# Test:
# curl -X POST -H "Content-Type:application/json" http://127.0.0.1:5000/Booking -d "{\"Dog_Name\":\"Jake\",\"Class_ID\":\"BOF1\",\"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\"}" - test working
@app.route('/Booking', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    Booking = {
        "Dog_Name": request.json['Dog_Name'],
        "Class_ID": request.json['Class_ID'],
        "Class_Name": request.json['Class_Name'],
        "Day": request.json['Day'],
        "Time": request.json['Time'],
        }
    return jsonify(bookingDao.create(Booking))
    

# Update the database:
# Test:
# curl -X PUT -d "{\"Dog_Name\":\"Jake\",\"Class_ID\":\"BOF1\",\"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\"}" -H "content-type:application/json" http://127.0.0.1:5000/Booking/Jake - test working
@app.route('/Booking/<Dog_Name>', methods=['PUT'])
def update(Dog_Name):
    foundBooking = bookingDao.findById(Dog_Name)
    if not foundBooking:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if foundBooking == {}:
        return jsonify({}), 404  
    currentBooking = foundBooking
 
    if 'Class_ID' in reqJson:
        currentBooking['Class_ID'] = reqJson['Class_ID']      
    if 'Class_Name' in reqJson:
        currentBooking['Class_Name'] = reqJson['Class_Name']
    if 'Day' in reqJson:
        currentBooking['Day'] = reqJson['Day']
    if 'Time' in reqJson:
        currentBooking['Time'] = reqJson['Time'] 
    return jsonify(currentBooking)
        
@app.route('/Booking/<Dog_Name>' , methods=['DELETE'])
def delete(Dog_Name):
    bookingDao.delete(Dog_Name)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)