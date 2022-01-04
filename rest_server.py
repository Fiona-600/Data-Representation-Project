from flask import Flask, jsonify, request, abort
from ClassesDao import classesDao
import os
from flask import send_from_directory

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Add favicon:
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'staticpages'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Check Connection:
# Test:
# curl "http://127.0.0.1:5000/Classes" - test working
@app.route('/')
def index():
    return "hello"


# Return all Classes:
# Test:
# curl "http://127.0.0.1:5000/Classes" - test working
@app.route('/Classes')
def getAll():
    #print("in getall")
    return jsonify(classesDao.getAll())

# Get by ID:
#curl "http://127.0.0.1:5000/Classes/ACW1" - test working
@app.route('/Classes/<Class_ID>')
def findById(Class_ID):
    return jsonify(classesDao.findById(Class_ID))   


# Create new class:
# Test:
# curl -X POST -H "Content-Type:application/json" http://127.0.0.1:5000/Classes -d "{\"Class_ID\":\"BOF\",\"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\", \"Max_Participants\":10, \"Trainer\":\"Orla\"}" - test working
@app.route('/Classes', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    Classes = {
        "Class_ID": request.json['Class_ID'],
        "Class_Name": request.json['Class_Name'],
        "Day": request.json['Day'],
        "Time": request.json['Time'],
        "Max_Participants": request.json['Max_Participants'],
        "Trainer": request.json['Trainer'],
    }
    print ("success")
    return jsonify(classesDao.create(Classes))
    

# Update the database:
# Test:
# curl -X PUT -d "{\"Class_ID\":\"BOFI\",\"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\", \"Max_Participants\":10, \"Trainer\":\"Orla\"}" -H "content-type:application/json" http://127.0.0.1:5000/Classes/BOF - test working
@app.route('/Classes/<Class_ID>', methods=['PUT'])
def update(Class_ID):
    foundClass = classesDao.findById(Class_ID)
    if not foundClass:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if foundClass == {}:
        return jsonify({}), 404  
    currentClass = foundClass
    if 'Max_Participants' in reqJson and type(reqJson['Max_Participants']) is not int:
        abort(400)
    if 'Class_Name' in reqJson:
        currentClass['Class_Name'] = reqJson['Class_Name']
    if 'Day' in reqJson:
        currentClass['Day'] = reqJson['Day']
    if 'Time' in reqJson:
        currentClass['Time'] = reqJson['Time']
    if 'Max_Participants' in reqJson:
        currentClass['Max_Participants'] = reqJson['Max_Participants']
    if 'Trainer' in reqJson:
        currentClass['Trainer'] = reqJson['Trainer']        

    return jsonify(currentClass)
        
@app.route('/Classes/<Class_ID>' , methods=['DELETE'])
def delete(Class_ID):
    classesDao.delete(Class_ID)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)