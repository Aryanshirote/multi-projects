from django.shortcuts import render

# REGISTRATION VIEW
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
            return render (request, "app4/registration.html", strmsg1)
    return render(request, "app4/registration.html")

# LOGIN VIEW
def login(request):
    return render(request, "app4/login.html")

# FOR PRACTICE DURING LECTURE 
db = [88,56,78,90,67,45,89,92,80,76]
def get_all_marks(request):
    context = {"marks": db}
    return render(request, "app4/display.html", context)
# ADDITION OF TWO NUMBERS
def add_two(request):
    if request.method=="POST":
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))

        res = num1 + num2

        context = {"result": res}
        return render (request, "app4/add.html", context)
    return render (request, "app4/add.html")

def substract(request):
    if request.method =="POST":
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))

        res = num1 - num2

        context = {"result1": res}
        return render(request, "app4/substract.html", context)
    return render(request, "app4/substract.html")
