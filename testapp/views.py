from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request, 'testapp/employees.html',data)
    return res

def greeting(request):
    s="<h1>Hello and Welcome to first view of test app </h1><P>This is a landing page</p>"
    return HttpResponse(s)

def showContact(request):
    s="<h1>Contct Page</h1>"
    s+="<p>Website: MySirrG.com</p>"
    s+="<p>Mobile Number: 9376369159</p>"
    return HttpResponse(s)
def about(request):
    text="This is an about Page"
    return render(request, 'testapp/about.html', {'text': text})
