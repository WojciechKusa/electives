from django.shortcuts import render

# Create your views here.
from obieraki.models import Student 
from django.contrib.auth import logout
from django.http import HttpResponse
#from obieraki.form import *


def main_site(request):
	return render(request, 'src/index.html', {})

def logout_page(request):
    logout(request)
    return render(request, "src/index.html", {})

def user_information(request):
    return render(request, "src/user_information.html", {})
'''
def register_page(request):
	template = get_template("register.html")
    form = RegisterForm()
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
	return render(request, "registration/register.html")
	'''