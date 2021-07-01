from os import name
import Project as ir
from flask import Flask , redirect, url_for,request
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def log():
    return render_template('home.html')

@app.route('/index',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        user = request.form['model']
        query=ir.writenumber(user)
        return "<h1>Statstical model</h1> <br>"+ir.Statistical_Model(query) 
 
@app.route('/weighted',methods=['POST','GET'])
def weighted():
    if request.method == 'POST':
        user = request.form['weighted']
        query=ir.unweighted(user)
        return "<h1>Vector Model</h1> <br>" +ir.calc_cosine(query)
 
@app.route('/generate',methods=['POST','GET'])
def generate():
    ir.CreateFiles()
    return "<h1> file generated successfully </h1>"

        
  
if __name__ == "__main__":
    app.debug = True
    app.run( )