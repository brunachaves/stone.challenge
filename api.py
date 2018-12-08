from flask import Flask, request, jsonify, redirect, session
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from dbfunc_setup import Employee, Base 
import os 
  

app = Flask(__name__) 
basedir = os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'employee.db') 
os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app) 
ma = Marshmallow(app) 

class EmployeeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'id', 'age', 'role')


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

@app.route("/") 
def mainmenu(): 
    return redirect("http://www.github.com/brunachaves/stone.challenge/blob/master/README.md", code=302)  

 

# endpoint to create new user 
@app.route("/employee", methods=["POST"]) 
def add_employee(): 
    name = request.form['name']
    age = request.form['age']
    role = request.form['role']
    
    new_employee = Employee(name = name, age = age, role = role)
    
    db.session.add(new_employee)
    db.session.commit()    


    return jsonify('Added!')



# endpoint to show all employees 
@app.route("/employee", methods=["GET"]) 
def get_employee(): 
    all_employee = db.session.query(Employee).all()
    result = employees_schema.dump(all_employee)
    
    return jsonify(result.data)

    
  

# endpoint to get employees detail by id 
@app.route("/employee/<employee_id>", methods=["GET"]) 
def employee_detail(employee_id): 
    employee = db.session.query(Employee).get(employee_id)

    return employee_schema.jsonify(employee)
  
  

# endpoint to update employee
@app.route("/employee/<employee_id>", methods=["PUT"]) 
def employee_update(employee_id): 
    employee = db.session.query(Employee).get(employee_id)
    name = request.form['name'] 
    age = request.form['age'] 
    role= request.form['role'] 
    employee.name = name
    employee.age = age
    employee.role = role

    db.session.add(employee)
    db.session.commit() 

    return ('Updated!')

  

# endpoint to delete employee
@app.route("/employee/<employee_id>", methods=["DELETE"]) 
def employee_delete(employee_id): 
    employee = db.session.query(Employee).get(employee_id) 

    db.session.delete(employee) 
    db.session.commit()   

    return ('Deleted!')

if __name__ == '__main__':
    app.run(debug=True)
