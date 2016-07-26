from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from .forms import JoinForm
from giref.models import SiteContent
from .models import TeenProject, Testimony,TestimonyType, Club, Student

# Create your views here.

def index(request):
	query_set_1 = SiteContent.objects.get(unique_name="CFYHomePage")
	query_set_2 = TeenProject.objects.all()[:3]
	query_set_T = Testimony.objects.filter(testimony_type = 1).order_by('-id')[:3]
	query_set_Teen = Testimony.objects.filter(testimony_type = 2).order_by('-id')[:3]
	query_set_V = Testimony.objects.filter(testimony_type = 3).order_by('-id')[:3]

	len_projects = TeenProject.objects.count()
	len_students = Student.objects.count()
	len_club = Club.objects.count()

	context = {
		"query_1" : query_set_1,
		"query_2" : query_set_2,
		"teachers" : query_set_T,
		"teenagers" : query_set_Teen,
		"volunteers" : query_set_V,
		"len_projects": len_projects,
		"len_students" : len_students,
		"len_club" : len_club,

	}
	return render(request, 'codefortheyoung/index.html', context)

def about(request):
	return render(request, 'codefortheyoung/about.html')

def join_us(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		print("sss")

	context = {
		"form":form
	}

	return render(request, 'codefortheyoung/join_us.html', context)
