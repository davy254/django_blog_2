from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# user registration form
def register(request):
    """"
    Function for registering new users
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username},your account has been created.You can now login.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form })
