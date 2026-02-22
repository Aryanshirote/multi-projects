from django.shortcuts import render

def user_registration(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cfm_password = request.POST.get("confirm_password")
        if password != cfm_password:
            strmsg = {"error": "Password do not match"}
            return render (request, "app4/registration.html", strmsg)
        else:
            strmsg1 = {"Success": "Registration Successful Please Login"}
            return render (request, "app4/login.html", strmsg1)
    return render(request, "app4/registration.html")
