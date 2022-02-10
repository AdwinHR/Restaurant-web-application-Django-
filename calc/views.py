from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
# Create your views here.
def home(request):

    if request.method=='POST':
        con=contact()
        name= request.POST.get['name']
        phone=request.POST.get['phone']
        print(name , phone)
        con.name= name
        con.phone=phone
        con.save()
        print(con.name ,con.phone)
        #return HttpResponse("<h>Hello<h> ")
    return render(request ,"index.html")

