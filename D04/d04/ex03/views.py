from django.shortcuts import render, HttpResponse

# Create your views here.
def ex03_django(request):
	return render(request, 'ex03/django.html')