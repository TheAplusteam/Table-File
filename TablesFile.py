#Table-File
#==========

"""
The People List Entity is a list of system users. It contains the User ID assigned to the user (provided by UNO), the user type (administrator, staff, user), and the password linked to the user account.
"""
class PeopleList (models.Model):
	
	User_ID = models.charField(max_length = 25) #The ID of the user
	User_Type = models.charField(max_length = 20) #Type of the user
	Password = models.charField(max_length = 25) #Password of the user account
	
	def _unicode_ (self):
		return self.User_ID
		
		
"""
The System Maintenance Logs Entity consists of the date when system maintenance is performed and the description of the maintenance that was done.
"""
class SystemLogs(models.Model):
	
	Maintenance_Date = models.dateField(max_length = 50) #Date and time of the maintenance
	Reason = models.charField(max_length = 300) #Description of the maintenance performed
	
	def _unicode_ (self):
		return self.Maintenance_Date
		
		
"""
The Network Maintenance Logs Entity consists of the date when network maintenance is performed and the description of the maintenance that was done.	
"""
class NetworkLogs(models.Model):
	
	Maintenance_Date = models.dateField(max_length = 50) #Date and time of the maintenance
	Reason = models.charField(max_length = 300)  #Description of the maintenance performed
	
	def _unicode_ (self):
		return self.Maintenance_Date
"""

"""
class Borrow_table(models.Model):
    Equipment_ID = models.CharField(max_length=30) #The ID of equipment that is borrowed
    User_ID = models.CharField(max_length=25)      #The user that is borrowing this equipment
    
    def __unicode__(self):
        return self.User_ID
"""

"""
class Reserved_table(models.Model):  
    Equipment_ID = models.CharField(max_length=30) #The ID of equipment that is reserved
    User_ID = models.CharField(max_length=25)      #The user that reserved this equipment
    Reserved_date = models.DateField()             #The date that the equipment was reserved
    
    def __unicode__(self):
        return self.User_ID
 
"""

"""
class Equipment_list(models.Model):
    Equipment_ID = models.CharField(max_length=30)       #The ID of equipment
    Equipment_Type = models.CharField(max_length = 50)   #The type of equipment 
    Equipment_Name = models.CharField(max_length = 30)   #Name of the equipment
    Equipment_Descrition=models.CharField(max_length=100)#Description of equipment 
    Brand = models.CharField(max_length=30)              #Equipment brand
    Count = models.BigIntegerField(max_length=3000)      #Count of each type of equipment
    
    def __unicode__(self):
        return self.Equipment_ID
    
