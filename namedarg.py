def connect(location,username,password,dbname,tbname,port):
	print("Location: ",location)
	print("Username: ",username)
	print("Password: ",password)
	print("DataBaseName: ",dbname)
	print("TableName: ",tbname)
	print("Port number: ",port)
if __name__ =='__main__':
	connect(port="007",location="189.162.1.0",username="suresh",password="kumar",dbname="employee details",tbname="emp")