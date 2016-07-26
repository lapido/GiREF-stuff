from django.contrib import admin
from .models import SiteContent, GirefProject
# Register your models here.

class SiteContentModel(admin.ModelAdmin):
	list_display = ["unique_name","header"]
	search_fields = ["unique_name"]
	class Meta:
		model = SiteContent

class GirefProjectModel(admin.ModelAdmin):
	class Meta:
		model = GirefProject

admin.site.register(SiteContent, SiteContentModel)
admin.site.register(GirefProject, GirefProjectModel)
