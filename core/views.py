from django.shortcuts import HttpResponseRedirect, render

# Create your views here.
def login(request):

    return render(request,'login.html',{})

def check(request):
    
    email=request.POST["email"]
    password=request.POST["password"]
    
    print(email,password)
    if email=='sujay@gmail.com' and password=="1":
        return render(request,'success.html',{})
    else :
        return render(request,'failure.html',{})