from django.contrib import admin
from .models import TeenProject,TestimonyType, Testimony, Club, Student
# Register your models here.

class TeenProjectModel(admin.ModelAdmin):
	list_display = ["name"]
	class Meta:
		model = TeenProject

admin.site.register(TeenProject, TeenProjectModel)
admin.site.register(TestimonyType)
admin.site.register(Testimony)
admin.site.register(Club)
admin.site.register(Student)