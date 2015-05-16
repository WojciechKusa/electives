from django.shortcuts import render

# Create your views here.
from obieraki.models import Student 
from django.contrib.auth import logout

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

def main_site(request):
	
	
	
	return render(request, 'src/index.html', {})
