from flask import Flask,render_template
from employedata import Employe

app=Flask(__name__)

getEmploye=Employe()

@app.route('/')
def em():
    return render_template('home.html')

@app.route('/home')
def hm():
    return render_template('home.html')

@app.route('/contactus')
def cnt():
    return render_template('contactus.html')

@app.route('/about')
def abt():
    return render_template('about.html')

@app.route('/employe')
def emp():
    return render_template('employe.html',myEmployeList=getEmploye)


if(__name__=='__main__'):
    app.run(debug=True)


