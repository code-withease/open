from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse
from .forms import *
# Create your views here.


# @login_required
def dashboard_page(request):
    return render(request,'users_pages/dashboard.html')

def order_page(request):
    return render(request,'users_pages/test.html')


def notification_page(request):
    print(request.path)
    return render(request,'users_pages/notification.html')


def payment_page(request):
    return render(request,'users_pages/payment.html')


def resales_page(request):
    return render(request,'users_pages/resales.html')


def document_page(request):
    return render(request,'users_pages/document.html')

def login_page(request):
    # return render(request,"")
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_user = authenticate(request, email=user.email, password=form.cleaned_data['password'])
            if auth_user is not None:
                login(request, auth_user)
                return redirect('/profile')
    else:
        form = UserForm()
    return render(request, 'users_pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('index')

def edit_profile(request):
    print(request.path)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        # print(form.cleaned_data['first_name'])
        print(request.POST)
        if form.is_valid():
            # Update the user instance with the form data
            user.first_name = form.cleaned_data['first_name']
            # print(user.first_name)
            user.last_name = form.cleaned_data['last_name']
            user.date_birth = form.cleaned_data['date_of_birth']
            user.mobile_phone = form.cleaned_data['mobile_phone']
            user.street_address = form.cleaned_data['street_address']
            user.postal_code = form.cleaned_data['postal_code']
            user.city = form.cleaned_data['city']
            user.country = form.cleaned_data['country']
            user.Favourite_national_team = form.cleaned_data['favourite_national_team']
            user.Favourite_city = form.cleaned_data['favourite_city']
            user.favourite_language = form.cleaned_data['favourite_language']
            user.club_coeur = form.cleaned_data['club_de_coeur']
            print()
            try:
                user.save()
                return redirect('/dashboard')
            except Exception as e:
                print(e)
            # if user.save():
                
            # else:
            #     return redirect('/register')
        else:
            # Handle the case when the form is not valid 
            print(form.errors) 
    else:
        form = UserProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_of_birth': user.date_birth,
            'mobile_phone': user.mobile_phone,
            'street_address': user.street_address,
            'postal_code': user.postal_code,
            'city': user.city,
            'country': user.country,
            'favourite_national_team': user.Favourite_national_team,
            'favourite_city': user.Favourite_city,
            'favourite_language': user.favourite_language,
            'club_de_coeur': user.club_coeur,
        })
    return render(request, 'users_pages/profile.html', {'form': form})