from flask import Flask,render_template,request
from flask.helpers import flash
import db, os, re
app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config["MONGO_DBNAME"] = 'Login'


@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        mob = request.form.get('mob')
        Age = request.form.get('Age')
        Rating = request.form.get('Rating')
        Grade =request.form.get('Grade')
        user = db.User()
        user.name = name
        user.email = email
        user.num = mob
        user.Age = int(Age)
        user.Rating = Rating
        user.Grade = Grade
        user.save()
        flash("Created Successfully")
    return render_template('create.html')
@app.route('/View',methods=['POST',"GET"])
def view():
    users = db.User.objects()
    return render_template('read.html',users=users)

@app.route('/Age',methods=['POST',"GET"])
def Age():
    Age = request.form.get('Age')
    users = db.User.objects(Age__gte=10)
    return render_template('age.html',users=users)    
   
@app.route('/Grade',methods=['POST',"GET"])
def Grade():
    Grade = request.form.get('Grade')
    users = db.User.objects()    
    users.Grade = Grade
    return render_template('grade.html',users=users)

@app.route('/Rating',methods=['POST',"GET"])
def Rating():
    Rating = request.form.get('Rating')
    users = db.User.objects()    
    users.Rating = Rating
    return render_template('rating.html',users=users)

@app.route('/Update',methods=['POST',"GET"])
def update():
    users = db.User.objects()
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        mob = request.form.get('mob')
        Age = request.form.get('Age')
        Rating = request.form.get('Rating')
        Grade =request.form.get('Grade')
        user = db.User.objects(name=name)
        user.update(name=name,email=email,num=mob,Age=Age,Rating=Rating,Grade=Grade)
        user1 = db.User.objects()
        flash("Updated Successfully")

    # else:
    #     name = request.form.get('name','email','age')
    #     user = db.User.objects(name=name)
    return render_template('update.html',res=users)

@app.route('/Delete',methods=['POST',"GET"])
def delete():
    users1 = db.User.objects()
    if request.method  == "POST":
        name = request.form.get('name')
        user = db.User.objects(name=name)
        user.delete()
        users1 = db.User.objects()
    return render_template('delete.html',res=users1)



if __name__ == "__main__":
    app.run(debug=True)                               