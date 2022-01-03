#Virtual Environment Set up
#https://askubuntu.com/questions/250442/django-installed-but-cant-import-django-in-python#:~:text=You%20can%20import%20django%20if%20you%20find%20the,is%20that%20something%27s%20wrong%20with%20your%20python%20installation.

from flask import Flask, jsonify, request, abort
from ClassesDao import classesDao
#import django

#from django.db import models
#from models import ConfigFile
import os
from flask import send_from_directory
#set DJANGO_SETTINGS_MODULE=mysite.settings
#django-admin runserver
#DEBUG = False
app = Flask(__name__, static_url_path='', static_folder='static pages')

#@app.route('/favicon.ico')
#def favicon():
    #return send_from_directory(os.path.join(app.root_path, 'static pages'),
                               #'favicon.ico', mimetype='image/vnd.microsoft.icon')

#import dbconfig as cfg
#from .models import ConfigFile


#import sys, os
#sys.path.insert(0, "/path/to/parent/of/courseware") # /home/projects/my-djproj

#import sys
#sys.path

#import django
#django.setup() 
#export DJANGO_SETTINGS_MODULE=mysite.settings

@app.route('/')
def index():
    return "hello"
#get all

#curl "http://127.0.0.1:5000/Classes" - working
@app.route('/Classes')
def getAll():
    #print("in getall")
    return jsonify(classesDao.getAll())
    #results = classesDao.getAll()
    #return jsonify(results)
    #return jsonify({})   

#curl "http://127.0.0.1:5000/Classes/ACW1" - working
@app.route('/Classes/<Class_ID>')
def findById(Class_ID):
    return jsonify(classesDao.findById(Class_ID))
    #foundClass = classesDao.findByID(Class_ID)
    #return jsonify(foundClass)
    

# create
# curl -X POST -d "{\"Class_ID\":\"BOFI\",\"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\", \"Max_Participants\":10, \"Trainer\":\"Orla\"}" -H Content-Type:application/json http://127.0.0.1:5000/Classes
# curl  -i -H "Content-Type:application/json" -X POST "{\"Class_ID\":\"BOF1\", \"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\", \"Max_Participants\":10, \"Trainer\":\"Orla\"}" http://127.0.0.1:5000/Classes
# curl -i -H 'Content-Type:application/json' -X Post-d '{"Class_ID":"BOF1", "Class_Name":"Beginners-Obedience","Day":"Friday", "Time":"6pm", "Max_Participants":"10", "Trainer":"Orla"}' http://127.0.0.1:5000/Classes
# curl -X POST -H 'Content-Type:application/json' http://127.0.0.1:5000/Classes -d '{"Class_ID":"BOF1", "Class_Name":"Beginners-Obedience","Day":"Friday", "Time":"6pm", "Max_Participants":"10", "Trainer":"Orla"}'

@app.route('/Classes', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    Classes = {
        "Class_ID": request.json['Class_ID'],
        "Class_Name": request.json['Class_Name'],
        "Day": request.json['Day'],
        "Time": request.json['Time'],
        "Max_Participants": request.json['Max_Participants'],
        "Trainer": request.json['Trainer'],
    }
    values = (Classes["Class_ID"], Classes["Class_Name"], Classes["Day"], Classes["Time"], Classes["Max_Participants"], Classes["Trainer"])
    #values =(book['Title'],book['Author'],book['Price'])
    #newId = classesDao.create(values)
    #Classes['Class_ID'] = newId
    #return jsonify(Classes)
    return jsonify(classesDao.create(Classes))

# update
# curl -X POST -d "{\"Class_ID\":\"BOFI\",\"Class_Name\":\"Beginners-Obedience\",\"Day\":\"Friday\", \"Time\":\"6pm\", \"Max_Participants\":10, \"Trainer\":\"Orla\"}" -H Content-Type:application/json http://127.0.0.1:5000/Classes
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
# curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1

@app.route('/Classes/<Class_ID>', methods=['PUT'])
def update(Class_ID):
    foundClass = classesDao.findByID(Class_ID)
    #print (foundClass)
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

    #values = (foundClass['Class_ID'], foundClass['Class_Name'],foundClass['Day'],foundClass['Time'],foundClass['Max_Participants'],foundClass['Trainer'])
    #classesDao.update(values)
    return jsonify(currentClass)
        
@app.route('/Classes/<Class_ID>' , methods=['DELETE'])
def delete(Class_ID):
    classesDao.delete(Class_ID)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)