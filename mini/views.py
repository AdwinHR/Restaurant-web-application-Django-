"""
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
    return render(request , 'index.html')
"""

from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth 
from .models import contact, reserve_table
# Create your views here.
def home(request):


    if request.method=='POST':
        
        
        username1 =request.POST['username1']
        email1 =request.POST['email1']
        phone1 =request.POST['phone1']
        tables_reserved=request.POST['tables_reserved']
        date=request.POST['date1']
        time=request.POST['time1']
        y=reserve_table.objects.create(name1=username1 ,email1=email1, phone1=phone1,tables_count=tables_reserved , date=date ,time=time  )
        y.save()
        print("done" , username1, email1 , phone1 , tables_reserved, date , time)

    
        return render(request ,"index.html" ,{'link' : 'http://127.0.0.1:8000/'})

   
    else:
       
        return render(request ,"index.html" ,{'link' : 'http://127.0.0.1:8000/register'})


def cal(selected):
    txt=selected
    a1,a2,a3,a4,a6,a5,a7,a8,a9,a10=0,0,0,0,0,0,0,0,0,0
    x = txt.split()

    print(x)

            

    for i in range(0,len(x)):
        print(x[i])
        try:
            try:
                if x[i]=="Chicken_Mandi,":
                    a1=125
            except:
                a1=0
            try:
                if x[i]=="Taj_Special_Nan-Korma":
                    a2=150
            except:
                a2=0
            try:
                if x[i]=="Shawarma_Roll":
                    a10=80
            except:
                a10=0
            try:
                if x[i]=="Noddles":
                    a9=80
            except:
                a9=0
            try:
                if x[i]=="Paneer_butter_masala":
                    a8=139
            except:
                a8=0

            try:
                if x[i]=="Chhole_Battori":
                    a7=190
            except:
                a7=0
            try:
                if x[i]=="Tomato_soup":
                    a6=180
            except:
                a6=0
            try:
                if x[i]=="Veg_Biryani":
                    a5=90
            except:
                a5=0
            try:
                if x[i]=="Tandoori_Chicken":
                    a4=180
            except:
                a4=0
            try:
                if x[i]=="Pizza":
                    a3=195
            except:
                a3=0
        except:
            pass

    sum=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
    return sum
    

def register(request):

    if request.method=='POST':
        
        
        username =request.POST['username']
        email =request.POST['email']
        phone =request.POST['phone']
        address=request.POST['address']
        selected=request.POST['selected']
        
        amount=cal(selected)
        y=contact.objects.create(name=username ,email=email, phone=phone, address=address ,selected=selected,amount=amount  )
        



        
        y.save()
        print(username , email, phone , address , selected)

    
        return render(request ,"index.html" ,{'link' : 'http://127.0.0.1:8000/'})
    else:
        return render(request ,"register.html")