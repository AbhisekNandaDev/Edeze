from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import training,CartTraining,Consulting,Webstore,CartWebstore
# Create your views here.

def index(request):

    return render (request,'index.html')

def success(request):
    print("working")
    return HttpResponse("this is a success page")


def register_user(request):

    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create(username=email,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.save()

        return redirect("/login/")

    return render(request,"register.html")


def login_user(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not User.objects.filter(username=email).exists():
            return HttpResponse("user not found")
        
        user = authenticate(username=email,password=password)

        if user is None :
            return HttpResponse("invalid password")
        else:
            login(request,user)
            return redirect("/home/")
        
    return render (request,"login.html")


def logout_user(request):

    logout(request)

    return redirect("/login/")

@login_required(login_url="/login/")
def home(request):

    return render(request,"home.html")

@login_required(login_url="/login/")
def training_page(request):

    crs = training.objects.all()
    context = {"crs":crs}
    return render (request,"training.html",context=context)

@login_required(login_url="/login/")
def training_details(request,id):

    cr=training.objects.filter(id=id)
    print(cr[0].course_name)
    context={"cr":cr[0]}
    return render(request,"training-detail.html",context=context)

@login_required(login_url="/login/")
def addtocart(request,user_id,course_id):
    CartTraining.objects.create(user_id=user_id,course_id=course_id)

    return redirect("/training/")

@login_required(login_url="/login/")
def cart(request,id):

    #EnrollCart
    crs = CartTraining.objects.filter(user_id=id)
    lst=[]
    enroll_price =0 
    for cr in crs:
        cr1=training.objects.filter(id=cr.course_id)
        enroll_price= cr1[0].course_price
        lst.append(cr1[0])

    #WebstoreCart
    webs = CartWebstore.objects.filter(user_id=id)
    lst_wb=[]
    web_price =0 
    for web in webs:
        web=Webstore.objects.filter(id=cr.course_id)
        web_price= web[0].web_price
        lst_wb.append(web[0])
    
    context = {"crs":lst,"enrollPrice":enroll_price,"webs":lst_wb,"webstorePrice":web_price}

    return render(request,"cart.html",context=context)

@login_required(login_url="/login/")
def consulting(request):
    cons = Consulting.objects.all()
    context={"cons":cons}

    return render(request,"consulting.html",context=context)

@login_required(login_url="/login/")
def consultingDetails(request,id):
    cons = Consulting.objects.filter(id=id)
    context={"con":cons[0]}

    return render (request,"consulting-detail.html",context=context)

@login_required(login_url="/login/")
def webstore(request):
    webs =  Webstore.objects.all()
    context = {"webs":webs}

    return render(request,"webstore.html",context=context)

@login_required(login_url="/login/")
def webstoreDetails(request,id):
    webs =  Webstore.objects.filter(id=id)
    context = {"webs":webs[0]}

    return render(request,"webstore-clicked.html",context=context)


@login_required(login_url="/login/")
def addtocartwebstore(request,user_id,course_id):
    print("hello")
    CartWebstore.objects.create(user_id=user_id,course_id=course_id)
    #return redirect("/webstore/")
    return redirect("/webstore/")


@login_required(login_url="/login/")
def about_us(request):
    print("about us")
    return render(request,"about_us_page.html")