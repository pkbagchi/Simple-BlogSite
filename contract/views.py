from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseServerError
from .forms import ContractForms

from django.contrib import messages

# Create your views here.

def Contract(request):
    form = ContractForms

    if request.method == 'POST':
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
          
          
    return render(request, 'contract.html', {'form':form})


