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

class WebsiteType(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return(self.name)

class Banner(models.Model):
	website = models.ForeignKey(WebsiteType, on_delete=models.CASCADE)
	page = models.CharField(max_length=50)
	image = models.FileField(null=False)
	caption = models.CharField(max_length=100, null=True, blank=True)
	slider = models.BooleanField("Is the Image part of a set of slider?",default=False)

