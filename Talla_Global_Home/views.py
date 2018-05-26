from django.shortcuts import render

from django.shortcuts import render, redirect

from . forms import RegistrationForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required



def home_page(request):

    return render(request, "home/homepage.html")

def features(request):

    return render(request, "home/features.html")

@login_required()
def deposit(request):

    return render(request, "home/deposit.html")

def contact(request):

    return render(request, "home/contact.html")

def licence(request):

    return render(request, "home/licence.html")
@login_required()
def member_home(request):

    return render(request, "home/member_home.html")

@login_required()
def member_contact(request):

    return render(request, "home/member_contact.html")

@login_required()
def cashout(request):

    return render(request, "home/cashout.html")

def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.save()


            messages.success(request, 'Registration successful.You can now log in with your username and password')

            return redirect('/accounts/login')

    else:
        form = RegistrationForm()


    return render(request, 'account/register.html', {'form':form})
