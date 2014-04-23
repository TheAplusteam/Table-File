Table-File
==========
from django.db import models



#The People List Entity is a list of system users. It contains the User ID assigned to the user (provided by UNO), the user type (administrator, staff, user), and the password linked to the user account.

class PeopleList (models.Model):

    User_ID = models.CharField(max_length = 25) #The ID of the user
    User_Type = models.CharField(max_length = 20) #Type of the user
    Password = models.CharField(max_length = 25) #Password of the user account
    def __unicode__(self):
        return self.User_ID



#The System Maintenance Logs Entity consists of the date when system maintenance is performed and the description of the maintenance that was done.

class SystemLogs(models.Model):

    Maintenance_Date = models.DateField() #Date and time of the maintenance
    Reason = models.CharField(max_length = 300) #Description of the maintenance performed

    def __unicode__(self):
        return self.Maintenance_Date


#The Network Maintenance Logs Entity consists of the date when network maintenance is performed and the description of the maintenance that was done.

class NetworkLogs(models.Model):

    Maintenance_Date = models.DateField() #Date and time of the maintenance
    Reason = models.CharField(max_length = 300) #Description of the maintenance performed

    def _unicode_ (self):
        return self.Maintenance_Date
# Create your models here.
class Borrow_table(models.Model):
    Equipment_ID = models.CharField(max_length=30) #The ID of equipment that is borrowed
    User_ID = models.CharField(max_length=25)      #The user that is borrowing this equipment
    
    def __unicode__(self):
        return self.User_ID
class Reserved_table(models.Model):  
    Equipment_ID = models.CharField(max_length=30) #The ID of equipment that is reserved
    User_ID = models.CharField(max_length=25)      #The user that reserved this equipment
    Reserved_date = models.DateField()             #The date that the equipment was reserved
    
    def __unicode__(self):
        return self.User_ID
        
class Equipment_list(models.Model):
    Equipment_ID = models.CharField(max_length=30)       #The ID of equipment
    Equipment_Type = models.CharField(max_length = 50)   #The type of equipment 
    Equipment_Name = models.CharField(max_length = 30)   #Name of the equipment
    Equipment_Descrition=models.CharField(max_length=100)#Description of equipment 
    Brand = models.CharField(max_length=30)              #Equipment brand
    Count = models.BigIntegerField(max_length=3000)      #Count of each type of equipment
    
    def __unicode__(self):
        return self.Equipment_ID
    # Create your models here.
#The Request List Entity consists of the User ID of the user who made the request, the Equipment ID of the item needing maintenance, and the description of the problem with the item."""

class Request_List(models.Model):
    User_ID = models.CharField (max_length = 25) #The ID of the user"""
    Equipment_ID = models.CharField (max_length = 30) #"""The ID of equipment that requires maintenance"""
    Description = models.CharField (max_length = 500)# """Description of the problem with the equipment"""
    
    def __unicode__(self):
        return self.User_ID
    
    

#"""The History List Entity consists of the Equipment ID and a history of equipment borrowed by the corresponding user, identified by the User ID."""
   
def __unicode__(self):
    Previous_Borrowers = models.CharField (max_length = 1000) #"""Array of ID numbers of users who have borrowed the equipment in the past"""
    Equipment_ID = models.CharField (max_length = 25) #"""The ID of the equipment"""
    
    def _unicode_(self):
        return self.Previous_Borrowers
    
    

#"""The Compatibility Table Entity consists of the type of equipment, a count of available equipment of a particular type, a compatibility number indicating what the equipment is compatible with, and the list of parts items that are compatible with the equipment."""

class Compatability_Table(models.Model):
    Equipment_Type = models.CharField (max_length = 70) #"""Type of Equipment"""
    Type_Counter = models.CharField (max_length = 20) #"""A counter of existing available items of that particular type in the system. This counter will be decremented every time an equipment item is borrowed and incremented every time an equipment item is returned"""
    Compatibility = models.CharField (max_length = 100)# """A number that is used to find all parts that work with the equipment"""
    List = models.CharField (max_length = 1000) #"""The output of parts that are compatible with a given equipment item"""
    
    def _unicode_(self):
        return self.Equipment_Type
    
    
    
    
class Block_table(models.Model):
  #"""Consists of user ID of blocked user and reason they have been
#blocked from borrowing."""
    User_ID = models.CharField(max_length=25) #User ID of user who is blocked from borrowing
    Block_Reason = models.CharField(max_length=500) #Reason user is blocked from borrowing

    def __unicode__(self):
        return self.User_ID


class Parts_table(models.Model):
#"""Consists of part name, compatibility of part, and count
#of each part in stock."""
    PartName = models.CharField(max_length=70) #Name of the part
    Compatibility = models.CharField(max_length=20) #Number assigned to all parts to show what equipment can use it.
    PartCounter = models.CharField(max_length=20) #Count of each part in stock

    def __unicode__(self):
        return self.PartName


class Software_table(models.Model):
#"""Consists of software name, compatibility of the software, ane
#count of each software in stock."""
    SoftName = models.CharField(max_length=70) #Name of software installed on piece of equipment
    Compatibility = models.CharField(max_length=20) #Number assigned to all software to show what equipment can use it.
    SoftCounter = models.CharField(max_length=20) #Count of software in stock

    def __unicode__(self):
        return self.SoftName


class BackupLogs_table(models.Model):
#"""Consists of a log of backups containing the date and description
#of each backup done on the system."""
    Backup_Date = models.DateField(max_length=50) #Date and time of backup
    Description = models.CharField(max_length=500) #Description of backup (scheduled, maintenance, etc.)

    def __unicode__(self):
        return self.Backup_Date

