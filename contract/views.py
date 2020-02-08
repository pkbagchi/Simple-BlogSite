from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseServerError
from .forms import ContractForms
import requests
import json

from django.contrib import messages

# Create your views here.

def Contract(request):
    form = ContractForms

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
            form = ContractForms(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data.get('name')
                names = name.split()
                name1 = name.split()

                if len(name1[0]) <= 3:
                    messages.success(request, f'Thanks, For your Feedback {names[1]}!')
                else:
                    messages.success(request, f'Thanks, For your Feedback {names[0]}!')

                return redirect('blog-home')
        else:
            messages.warning(request, 'Invalid reCaptcha!')
            return redirect('contract')
          
          
    return render(request, 'contract.html', {'form':form})


