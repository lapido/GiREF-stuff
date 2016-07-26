from django.db import models

# Create your models here.
class SiteContent(models.Model):
	header = models.CharField(max_length=30)
	unique_name = models.CharField(max_length=30)
	content = models.TextField()

	def __str__(self):
		return(self.unique_name)


class GirefProject(models.Model):
	header  = models.CharField(max_length=30)
	content = models.TextField()
	image = models.FileField(null=False)

	def __str__(self):
		return(self.header)