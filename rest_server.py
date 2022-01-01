#Virtual Environment Set up
#https://askubuntu.com/questions/250442/django-installed-but-cant-import-django-in-python#:~:text=You%20can%20import%20django%20if%20you%20find%20the,is%20that%20something%27s%20wrong%20with%20your%20python%20installation.

from flask import Flask, jsonify, request, abort
from ClassesDao import classesDao

#import dbconfig as cfg
#from .models import ConfigFile


#import sys, os
#sys.path.insert(0, "/path/to/parent/of/courseware") # /home/projects/my-djproj

#import sys
#sys.path

#import django
#django.setup() 
#export DJANGO_SETTINGS_MODULE=mysite.settings

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return "hello"
#get all

#curl "http://127.0.0.1:5000/Classes"
@app.route('/Classes')
def getAll():
    #print("in getall")
    return jsonify(classesDao.getAll())
    #results = classesDao.getAll()
    #return jsonify(results)

#curl "http://127.0.0.1:5000/Classes/2"
@app.route('/Classes/<int:ID>')
def findById(ID):
    return jsonify(classesDao.findById(ID))
    #foundClass = classesDao.findByID(ID)
    #return jsonify(foundClass)

# create
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
   

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/Classes', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    Classes = {
        "Class_Name": request.json['Class_Name'],
        "Day": request.json['Day'],
        "Time": request.json['Time'],
        "Max_Participants": request.json['Max_Participants'],
        "Trainer": request.json['Trainer'],
    }
    values = (Classes["ID"], Classes["Class_Name"], Classes["Day"], Classes["Time"], Classes["Max_participants"], Classes["Trainer"])
    #values =(book['Title'],book['Author'],book['Price'])
    #newId = classesDao.create(values)
    #Classes['ID'] = newId
    #return jsonify(Classes)
    return jsonify(classesDao.create(Classes))
    #return "served by Create "   

# update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
   

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/Classes/<int:ID>', methods=['PUT'])
def update(ID):
    foundClass = classesDao.findByID(ID)
    #print (foundClass)
    #if not foundClass:
        #abort(404)   
    #if not request.json:
        #abort(400)
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

    #values = (foundClass['id'], foundClass['Class_Name'],foundClass['Day'],foundClass['Time'],foundClass['Max_Participants'],foundClass['Trainer'])
    #classesDao.update(values)
    return jsonify(currentClass)
        

    

@app.route('/Classes/<int:ID>' , methods=['DELETE'])
def delete(ID):
    classesDao.delete(ID)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)