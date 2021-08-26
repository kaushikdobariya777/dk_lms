from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showTest(request):
    que="Who developed C language?"
    a="Kaushik"
    b="Nirupa"
    c="Aradhya"
    d="Luv"
    level="Easy"
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res

def showResult(request):
    s="<h2>This is Show Result Page</h2>"
    return HttpResponse(s)
