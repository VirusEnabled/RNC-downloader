import os,pymysql
"""
this file generates  a database in mysql 
and some other scripts.	
"""
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
			self.conector = pymysql.Connect('localhost',self.user,self.password,self.db)  # this one only works on Ubuntu and windows.

			#login_db=pymysql.Connect('127.0.0.1',"root",'Dontwasteourtime99%','GUI_DB',unix_socket="/var/lib/mysql/mysql.sock")
			self.query = ""
			self.exe = self.conector.cursor()
			self.status = True
			return self.status

		except pymysql.err.OperationalError:
			os.system("service mariadb start")
			self.connect()
			pass


		except pymysql.err.InternalError:
			print("the specified Database doesn't exist.")


		except Exception as ex:
			raise ex

	def generate_table(self):
		try:
			if self.status is True:

				self.query="drop table if exists rnc_info;"
				self.exe.execute(self.query)
				self.conector.commit()

				self.query ="create table rnc_info(id int not null,name varchar(100) null,business_name varchar(100) null,descripton varchar(200) null default 'NO DESCRIPCION',unknown_value1 varchar(100) null,unknown_value2 varchar(100) null,rnc int null,registration_date date not null,business_status varchar(100) not null,payment_method varchar(100) not null,constraint pkid primary key(id));"
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
			self.query = """LOAD DATA INFILE %s INTO TABLE rnc_info FIELDS TERMINATED BY ',' LINE TERMINATED BY '\n';""" % path_file
			self.exe.execute(self.query)
			self.conector.commit()
			return "Success"
		except Exception as ex2:
			raise ex2
			input("press enter to exit")


		
if __name__ == '__main__':
	db=DbManager("rnc_db","root","Dontwasteourtime99%")
	print(db.connect())
	#print(db.automated_data_loader(df.file_formater(df.unzipper("%s/DGII_RNC.zip" % os.getcwd()))))
