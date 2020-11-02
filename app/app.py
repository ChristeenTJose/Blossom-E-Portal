from flask import Flask,render_template,redirect,url_for,request,session

import crud

app = Flask(__name__)
app.secret_key = "super secret key"
		
@app.route("/")
def index():
	if "SIGNED_IN" in session and session["SIGNED_IN"] == True:
		return render_template("templateIndexBody1SignOut.html")
	else:
		return render_template("templateIndexBody1.html")
		
'''
	Admin Pages:
'''	
	
@app.route("/admin/",methods = ["GET","POST"])
def admin():
	if request.method == "POST":
		username = request.form["uname"]
		password = request.form["psw"]
		Username, Password = crud.get_admin()
		if username == Username and password == Password:
			session["ADMIN_SIGNED_IN"]= True
		return redirect(url_for('admin'))
		
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminMain.html")
	else:
		return render_template("adminSignIn.html")

@app.route("/admin/view/")
def adminView():
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		results = crud.get_bookings()
		if results == -1:
			return render_template("templateAdminView.html")
		else:
			return render_template("templateAdminView.html", bookings = results)
	else:
		return render_template("adminSignIn.html")

@app.route("/admin/search/",methods = ["GET","POST"])
def adminSearch():
	if request.method == "POST":
		course = request.form["cname"]
		results = crud.get_course(course)
		if results == -1:
			found = "No course named '"+course+"' was found"
			return render_template("templateAdminNoResult.html",found=found)
		else:
			found = "Course Details:"
			return render_template("templateAdminSearchResult.html",found=found,results=results)
			
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminSearch.html")
	else:
		return render_template("adminSignIn.html")
		
@app.route("/admin/add/",methods = ["GET","POST"])
def adminAdd():
	if request.method == "POST":
		courseName = request.form["cname"]
		price = request.form["price"]
		courseDescription = request.form["about"]
		crud.set_course(courseName,price,courseDescription)
		found = "Course has been added successfully"
		return render_template("templateAdminNoResult.html",found=found)
			
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminAdd.html")
	else:
		return render_template("adminSignIn.html")

@app.route("/admin/update/")
def adminUpdate():
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminUpdate.html")
	else:
		return render_template("adminSignIn.html")

@app.route("/admin/update/course/",methods = ["GET","POST"])
def adminUpdateCourse():
	if request.method == "POST":
		courseName = request.form["cname"]
		return render_template("templateAdminUpdateCourse.html",course=courseName)
		
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminUpdate.html")
	else:
		return render_template("adminSignIn.html")
		
@app.route("/admin/update/course/<course>/",methods = ["GET","POST"])
def adminUpdateCourseResult(course):
	if request.method == "POST":
		price = request.form["price"]
		courseDescription = request.form["about"]
		crud.update_course(course,price,courseDescription)
		found = "Course has been updated successfully"
		return render_template("templateAdminNoResult.html",found=found)
		
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminUpdate.html")
	else:
		return render_template("adminSignIn.html")
		
@app.route("/admin/delete/",methods = ["GET","POST"])
def adminDelete():
	if request.method == "POST":
		course = request.form["cname"]
		results = crud.get_course(course)
		if results == -1:
			found = "No course named '"+course+"' was found"
			return render_template("templateAdminNoResult.html",found=found)
		else:
			crud.delete_course(course)
			found = "Course has been deleted successfully"
			return render_template("templateAdminNoResult.html",found=found)
			
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminDelete.html")
	else:
		return render_template("adminSignIn.html")
		
@app.route("/admin/find/",methods = ["GET","POST"])
def adminFind():
	if request.method == "POST":
		username = request.form["uname"]
		results = crud.get_user(username)
		if results == -1:
			found = "No users found for username: " + username
			return render_template("templateAdminNoResult.html",found=found)
		else:
			found = "Contact Details:"
			return render_template("templateAdminFindResult.html",found=found,results=results)
			
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		return render_template("templateAdminFind.html")
	else:
		return render_template("adminSignIn.html")
		
@app.route("/admin/logout/")
def adminLogOut():
	if "ADMIN_SIGNED_IN" in session and session["ADMIN_SIGNED_IN"] == True:
		session["ADMIN_SIGNED_IN"]= False
		return redirect(url_for("admin"))
	else:
		return render_template("adminSignIn.html")
		
'''
	User Pages:
'''	
	
@app.route('/SignIn/',methods = ["GET","POST"])
def SignIn():
	if request.method == "POST":
		username = request.form["uname"]
		password = request.form["psw"]
		
		results = crud.get_user(username)
		if results != -1:
			if username == results["username"] and password == results["password"]:
				session["SIGNED_IN"] = True
				session["Username"] = username
	
	if "SIGNED_IN" in session and session["SIGNED_IN"] == True:
		return redirect(url_for('index'))
	else:
		return render_template("templateIndexBody2.html")

@app.route('/SignUp/',methods = ["GET","POST"])	
def SignUp():
	if request.method == "POST":
		username = request.form["uname"]
		password = request.form["psw"]
		phone = request.form["phone"]
		email = request.form["email"]
		
		crud.set_user(username,password,phone,email)
		session["SIGNED_IN"] = True
		session["Username"] = username
		
	return redirect(url_for('index'))

@app.route("/SignOut/")
def SignOut():
	if "SIGNED_IN" in session and session["SIGNED_IN"] == True:
		session["SIGNED_IN"] = False	
	return redirect(url_for('index'))
	
@app.route('/course/<cName>/')
def course(cName):
	if "SIGNED_IN" in session and session["SIGNED_IN"] == True:
		course = crud.get_course(cName)
		if course != -1:
			booking = crud.get_booking(course["courseName"],session["Username"])
			if booking == -1:
				disabled = ""
				Book = "Book"
			else:
				disabled = "disabled"
				Book="Booked"
			return render_template("templateCourse.html",courseName=course["courseName"],price=course["price"],courseDescription=course["courseDescription"],username=session["Username"],disabled = disabled, Book = Book)	
		else:
			return redirect(url_for('index'))
	return redirect(url_for('SignIn'))

@app.route('/course/<cName>/<uName>')
def booking(cName,uName):
	if "SIGNED_IN" in session and session["SIGNED_IN"] == True:
		crud.set_booking(cName,uName)
		return '<button class="btn" onclick="book()" disabled>Booked</button>'
	else:	
		return redirect(url_for('SignIn'))	
		
if __name__ == "__main__":
	app.run(debug=True)
