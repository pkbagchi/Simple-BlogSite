from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegForm, UserUpdate
from django.contrib.auth.decorators import login_required
import requests
import json


# Create your views here.

def register(request):
    
    if request.method == 'POST':
        clientkey = request.POST['g-recaptcha-response']
        secretkey = ''
        capthchaData = {
            'secret': secretkey,
            'response' : clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = capthchaData)
        response = json.loads(r.text)
        verify = response['success']
        if verify:
            form = UserRegForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Welcome {username}, Please Login!')
                return redirect('login')
        else:
            messages.warning(request, 'Invalid reCaptcha!')
            return redirect('register')
          
    else:
        form = UserRegForm()

    return render(request, 'register.html', {'form':form})


# def handler404(request,Exception):
#     return render(request, '404.html', status=404)

# def error_page(request):
#     return render(request,'404.html')


@login_required
def profile(request):

    if request.method == "POST":
        
        u_form = UserUpdate(request.POST, instance = request.user)
        #p_form = ProfileUpdate(request.POST,
         #                          request.FILES,
          #                         instance=request.user.profile)

        if u_form.is_valid():
            u_form.save()
            #p_form.save()
            messages.success(request, "Your Acoount has been Updated!")
            return redirect('blog-home')

    else:
        u_form = UserUpdate(instance = request.user)
       # p_form = ProfileUpdate(instance=request.user.profile)

    
    context = {
        'u_form':u_form,
        #'p_form':p_form
    }

    return render(request, 'profile.html',context)
