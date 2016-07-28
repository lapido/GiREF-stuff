from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from .forms import JoinForm
from giref.models import SiteContent, WebsiteType, Banner
from .models import TeenProject, Testimony,TestimonyType, Club, Student

# Create your views here.

def index(request):
	query_set_1 = SiteContent.objects.get(unique_name="CFYHomePage")
	query_set_2 = TeenProject.objects.all()[:3]
	query_set_T = Testimony.objects.filter(testimony_type = 1).order_by('-id')[:3]
	query_set_Teen = Testimony.objects.filter(testimony_type = 2).order_by('-id')[:3]
	query_set_V = Testimony.objects.filter(testimony_type = 3).order_by('-id')[:3]
	query_set_b = Banner.objects.filter(slider=True).order_by('-id')

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
		"slides":query_set_b,

	}
	return render(request, 'codefortheyoung/index.html', context)

def about(request):
	return render(request, 'codefortheyoung/about.html')

def join(request):
	return render(request, 'codefortheyoung/join.html')	

def join_us(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		first_name = forms.cleaned_data['first_name']
		last_name = forms.cleaned_data['last_name']
		email = forms.cleaned_data['email']
		country = forms.cleaned_data['country']
		state = forms.cleaned_data['state']
		phoneNumber = forms.cleaned_data['phonenumber']

		subject = 'Codefortheyoung: Interest Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]

		message = """
			First Name: %s \n
			Last Name: %s \n
			Email Address: %s \n
			Country: %s \n
			State: %s \n
			Phone Number: %s \n
		""" %(first_name,
			last_name,
			email,
			country,
			state,
			phonenumber)
		email_state = send_mail(subject, message, from_email, to_email,fail_silently=False)

		if email_state:
			state = "confirm"
			context = {
				state:state
			}
			render(request, 'codefortheyoung/join.html', context)
		else:
			state = "error"
			render(request, 'codefortheyoung/join.html', context)

	context = {
		"form":form
	}

	return render(request, 'codefortheyoung/join_us.html', context)
