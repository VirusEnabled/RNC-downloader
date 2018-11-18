from flask import Flask,render_template,send_file,url_for
from flask_mysqldb import MySQL
from urllib import request
from OffDependencies import data_fixer as dx
import os,requests,zipfile
from rnc_downloader import rnc_grabber



app = Flask("__name__")
app.config["MYSQL_HOST"] = "localhost" # host where the code is going to run
app.config["MYSQL_USER"] = "rnc_viewer"  #user in mysql
app.config["MYSQL_PASSWORD"] = "Password22"  #Password of the user
app.config["MYSQL_DB"] = "rnc_db"  #Name of the database
#app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mydb = MySQL(app)

# Mysql init


def automated_data_loader(path_file):

	"""
	this method loads the information from
	the file into the table automatically 
	just by using a mysql sentence.
	"""
	try:
		query = """LOAD DATA LOCAL INFILE '%s' INTO TABLE rnc_info FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';""" % path_file
		exe = mydb.connection.cursor()
		exe.execute(query)
		mydb.connection.commit()
		#mydb.connection.close()
		os.remove("%s" % path_file)
		os.system("rm -r -f TMP")
		return True, ""
	except Exception as ex2:
		return False,ex2


@app.route("/")
def home():
	return render_template("home.html")


# it needs to be debugged. for real.
def download():
	"""
	this is an alternative way 
	of downloading the file form the web
	as flask.request library doesn't do
	the job and uploads the file into the server.
	"""
	return rnc_grabber()


@app.route("/contact")
def contact():
	return render_template("Contact.html")


@app.route("/downloaded_info")
def showing_results():
	"""
	This method downloads a file from the web.
	returns a result page with has as content the
	decoded information in a table.
	"""
	
	file = download()
	#formated_file = dx.file_formater(dx.unzipper(file[1]))\
	# testing_file = "%s/DGII_RNC.zip" % os.getcwd()  # this file is used for testing purposes as the downloader func. ain' working properly
	formated_file = dx.file_formater(dx.unzipper(file))
	inserted = automated_data_loader(formated_file)
	#@after_this_request
	if inserted[0] is True:
		my_cursor = mydb.connection.cursor()
		query = """select id,owner_name,business_name,descripton,management, location,district,
					employees_amount,phone_number,registration_date,payment_method,status
					from rnc_info where employees_amount != 0 and registration_date!="0000-00-00" limit 40;"""
		my_cursor.execute(query)
		resulting_data_gathered = my_cursor.fetchall()
		#resulting_data_gathered = [value for element in resulting_data_gathered for key,value in element.items()]
		#mydb.connection.close()
		return render_template("results.html",resulting_data_gathered=resulting_data_gathered)
	return render_template("results.html",error=inserted[1])


if __name__ == '__main__':
	app.run(debug = True)
