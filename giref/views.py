from django.conf import settings
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


from .models import SiteContent, GirefProject

# Create your views here.
def index(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	query_set = SiteContent.objects.get(unique_name="giref_home_about")
	
	query_set_2 = GirefProject.objects.all()
	context = {
		"object_list":query_set,
		"giref_project":query_set_2,
		"title":"GiREF",
		
	}
	return render(request, 'giref/index.html', context)

def about_us(request):
	query_set_3 = SiteContent.objects.get(unique_name="giref_mission")
	query_set_4 = SiteContent.objects.get(unique_name="giref_vision")
	query_set_5 = SiteContent.objects.get(unique_name="giref_about")

	context = {
		"mission":query_set_3,
		"vision":query_set_4,
		"about" : query_set_5,
	}
	return render(request, 'giref/about-us.html', context)


def try_home(request):
	return render(request, 'giref/about_us.html')

def contact_us(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():

		form_message = form.cleaned_data['message']
		form_sender = form.cleaned_data['sender']
		first_name = form.cleaned_data['first_name']
		second_name = form.cleaned_data['second_name']
		form_name = str(first_name + " " + second_name)
		
		subject = 'GiREF contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s : %s via %s" %(
			form_name,
			form_message,
			form_sender
			)

		send_mail(subject, contact_message, from_email, to_email,fail_silently=False)

	context = {
		"form":form,
	}
	return render(request, 'giref/contact-us.html', context)

def join_us(request):
	return render(request, 'giref/join-us.html')

	
	