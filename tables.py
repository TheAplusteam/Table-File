Table-File
==========
from django.db import models

class Block_table(models.Model):
  """Consists of user ID of blocked user and reason they have been
	   blocked from borrowing."""
	User_ID = models.CharField(max_length=25) #User ID of user who is blocked from borrowing
	Block_Reason = models.CharField(max_length=500) #Reason user is blocked from borrowing

	def __unicode__(self):
		return self.User_ID


class Parts_table(models.Model):
	"""Consists of part name, compatibility of part, and count
	   of each part in stock."""
	PartName = models.CharField(max_length=70) #Name of the part
	Compatibility = models.CharField(max_length=20) #Number assigned to all parts to show what equipment can use it.
	PartCounter = models.CharField(max_length=20) #Count of each part in stock
	
	def __unicode__(self):
		return self.PartName


class Software_table(models.Model):
	"""Consists of software name, compatibility of the software, ane
	   count of each software in stock."""
	SoftName = models.CharField(max_length=70) #Name of software installed on piece of equipment
	Compatibility = models.CharField(max_length=20) #Number assigned to all software to show what equipment can use it.
	SoftCounter = models.CharField(max_length=20) #Count of software in stock

	def __unicode__(self):
		return self.SoftName


class BackupLogs_table(models.Model):
	"""Consists of a log of backups containing the date and description
	   of each backup done on the system."""
	Backup_Date = models.DateField(max_length=50) #Date and time of backup
	Description = models.CharField(max_length=500) #Description of backup (scheduled, maintenance, etc.)

	def __unicode__(self):
		return self.Backup_Date
