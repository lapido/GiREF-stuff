from django.db import models

# Create your models here.
class TeenProject(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()
	image = models.FileField(null=False)


	def __str__(self):
		return(self.name)


class TestimonyType(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return(self.name)

class Testimony(models.Model):
	testimony_type = models.ForeignKey(TestimonyType, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	content = models.TextField()
	image = models.FileField(null=False)
	
	def __str__(self):
		return(self.name)
	

class Club(models.Model):
	name = models.CharField(max_length=200)
	country = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	address = models.TextField()
	coordinator = models.CharField(max_length=100)

class Student(models.Model):
	name = models.CharField(max_length=100)
	country = models.CharField(max_length = 100)
	state = models.CharField(max_length=100)
	school_name = models.CharField(max_length=200)
	age = models.IntegerField()
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	
