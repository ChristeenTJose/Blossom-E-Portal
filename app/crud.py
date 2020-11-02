import pymongo

from courses import courses

USERNAME = "" #Set Username
PASSWORD = "" #Set Password

CLUSTER = pymongo.MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.toftl.mongodb.net/<dbname>?retryWrites=true&w=majority")
DB = CLUSTER["Blossom"]

def set_admin(usr = "Admin@Blossom",psw = "Admin@Blossom"):
	collection = DB["Admin"]
	collection.delete_many({})
	post = {"_id": 0, "username": usr, "password": psw}
	collection.insert_one(post)

def get_admin():
	collection = DB["Admin"]
	results = collection.find_one({})	
	return results["username"],results["password"]

def set_user(username,password,phone,email):
	collection = DB["Users"]
	post = {"username": username, "password": password, "phone": phone, "email": email}
	collection.insert_one(post)

def get_user(username):
	collection = DB["Users"]
	results = collection.find_one({"username":username})
	if results is None:
		return -1
	else:
		return results
		
def set_booking(course,username):
	collection = DB["Bookings"]
	post = {"course": course,"username": username}
	collection.insert_one(post)

def get_booking(course,username):
	collection = DB["Bookings"]
	results = collection.find_one({"course": course,"username": username})
	if results is None:
		return -1
	else:
		return results

def get_bookings():
	collection = DB["Bookings"]
	results = collection.find({})
	if results is None:
		return -1
	else:
		return results

def reset_bookings():
	collection = DB["Bookings"]
	collection.delete_many({})
	
def set_courses():
	collection = DB["Courses"]
	collection.delete_many({})
	collection.insert_many(courses)
	
def set_course(courseName,price,courseDescription):
	collection = DB["Courses"]
	post = {"courseName": courseName, "price": price, "courseDescription": courseDescription}
	collection.insert_one(post)

def update_course(course,price,courseDescription):
	collection = DB["Courses"]
	collection.update_one({"courseName": course},{"$set":{"price": price, "courseDescription": courseDescription}})	

def get_course(course):
	collection = DB["Courses"]
	results = collection.find_one({"courseName": course})
	if results is None:
		return -1
	else:
		return results

def delete_course(course):
	collection = DB["Courses"]
	collection.delete_one({"courseName": course})
	
def get_courses():
	collection = DB["Courses"]
	results = collection.find({})
	if results is None:
		return -1
	else:
		return results

if __name__ == "__main__":
	#set_admin()
	set_courses()
	reset_bookings()
