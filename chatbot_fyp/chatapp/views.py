from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from .forms import ContactForm

# from .bot import agent

def home_view(request):
	return render(request, 'chat/index.html')

def admission_view(request):
	return render(request, 'chat/admission.html')

def course_view(request):
	return	render(request,'chat/course.html')

def about_view(request):
	return render(request, 'chat/about.html')

def contact_view(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContactForm()
		context = {
			'form': form
		}
	else:
		form = ContactForm()

	return render(request, 'chat/contact.html',{'form': form})

@csrf_exempt
def webhook(request):
	print(request.POST)
	return JsonResponse({"status": "OK"})