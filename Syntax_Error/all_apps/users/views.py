from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def sign_up(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        user_email=request.POST.get('email-id')
        user_first_name=request.POST.get('first-name')
        user_last_name=request.POST.get('last-name')
        user_pass1=request.POST.get('Password')
        user_pass2=request.POST.get('Confirm-Password')
        print(user_email,user_first_name,user_name)
        
    else:
        pass

