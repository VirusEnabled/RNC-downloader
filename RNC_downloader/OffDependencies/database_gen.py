import os,MySQLdb
"""
this file generates  a database in mysql 
and some other scripts.	
"""
#Usable
class DbManager(object):

	def __init__(self,database,user,password):
		self.db = database
		self.user = user
		self.password = password
		self.status = False

		pass
	

	def connect(self):
		try:
			#self.conector = pymysql.Connect('localhost',self.user,self.password,self.db,unix_socket="/var/lib/mysql/mysql.sock")
			self.conector = MySQLdb.Connect('localhost',self.user,self.password,self.db)  # this one only works on Ubuntu and windows.

			#login_db=pymysql.Connect('127.0.0.1',"root",'Dontwasteourtime99%','GUI_DB',unix_socket="/var/lib/mysql/mysql.sock")
			self.query = ""
			self.exe = self.conector.cursor()
			self.status = True
			return self.conector,self.status

		except MySQLdb.OperationalError as ex:
			self.status = False

		except MySQLdb.InternalError:
			print("the specified Database doesn't exist.")


		except Exception as ex:
			raise ex


	def generate_table(self):
		try:
			if self.status is True:

				self.query="drop table if exists rnc_info;"
				self.exe.execute(self.query)
				self.conector.commit()

				self.query ="create table rnc_info(id int not null ,owner_name varchar(100) not null,business_name varchar(100) not null,descripton varchar(200) not null default 'NO DESCRIPCION',management varchar(100) not null,location varchar(200) not null,employees_amount int not null,district varchar(100)not null,phone_number varchar(30) not null,registration_date date not null,status varchar(100) not null,payment_method varchar(100) not null,constraint pkid primary key(id));"

				self.exe.execute(self.query)
				self.conector.commit()
	
				return True
			else:
				raise NotImplementedError(" MySQL server must be running in order to generate the database")


		except Exception as e:
			raise e

	

	def query_inserter(self,table,param):
		"""
		creates a query and insert the data in the specified table

		"""
		try:
			self.query = "insert into %s values(%s);" % (table,param)
			self.exe.execute(self.query)
			self.conector.commit()
			return True
					
		except Exception as e:
			return False,e
	


	def automated_data_loader(self,path_file):

		"""
		this method loads the information from
		the file into the table automatically 
		just by using a mysql sentence.
		"""
		try:
			self.query = """LOAD DATA LOCAL INFILE '%s' INTO TABLE rnc_info FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';""" % path_file
			self.exe.execute(self.query)
			self.conector.commit()
			return True
		except Exception as ex2:
			return False,ex2
			input("press enter to exit")

	def showing_results(self):
		"""
		this method returns the top 20
		rows of the inserted data by the func.
		inserter
		"""
		try:
			self.query = """ select * from rnc_info where registration_date != "0000-00-00" limit 20;"""
			self.exe.execute(self.query)
			data = self.exe.fetchall()
			return data


		except Exception as e:
			raise e

	pass



		
if __name__ == '__main__':
	db=DbManager("rnc_db","rnc_viewer","Password22")
	print(db.connect(),db.showing_results(),type(db.showing_results()))
	#print(db.automated_data_loader(df.file_formater(df.unzipper("%s/DGII_RNC.zip" % os.getcwd()))))
