import pickle

class UserData:
	def __init__(self):
		self.name = 'None'
		self.password='None'
		self.gender = 'None'

	def extractData(self):
		with open('userData/userData.pck', 'rb') as file:
			details = pickle.load(file)
			self.name, self.password, self.gender = details['name'],details['password'], details['gender']
 
	def updateData(self, name,password, gender):
		with open('userData/userData.pck', 'wb') as file:
			details = {'name': name,'password': password ,'gender': gender}
			pickle.dump(details, file)

	def getName(self):
		return self.name

	def getPass(self):
		return self.password

	def getGender(self):
		return self.gender


def UpdateUserPhoto():
	u = UserData()
	u.extractData()
	u.updateData(u.getName(),u.getPass(), u.getGender())
