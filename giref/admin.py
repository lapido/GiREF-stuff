from django.contrib import admin
from .models import SiteContent, GirefProject, WebsiteType, Banner
# Register your models here.

class SiteContentModel(admin.ModelAdmin):
	list_display = ["unique_name","header"]
	search_fields = ["unique_name"]
	class Meta:
		model = SiteContent

class GirefProjectModel(admin.ModelAdmin):
	class Meta:
		model = GirefProject

class BannerModel(admin.ModelAdmin):
	list_display = ['page', 'website']
	class Meta:
		model = Banner

admin.site.register(SiteContent, SiteContentModel)
admin.site.register(GirefProject, GirefProjectModel)
admin.site.register(Banner, BannerModel)