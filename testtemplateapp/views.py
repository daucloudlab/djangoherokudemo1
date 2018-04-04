from django.shortcuts import render, redirect
from testtemplateapp.models import FeedBack
from testtemplateapp import forms

# Create your views here.

def home(request):
    feeds = FeedBack.objects.all()
    return render(request, 'testtemplateapp/index.html', {'feeds':feeds})


def feedback(request):
    if request.method == 'POST':
        feedform = forms.FeedForm(request.POST)
        if feedform.is_valid():
            firstname = feedform.cleaned_data['firstname']
            lastname = feedform.cleaned_data['lastname']
            email = feedform.cleaned_data['email']
            feedback = FeedBack.objects.create(first_name=firstname, last_name=lastname,
                                email=email)
        return redirect('/')
    else:
        feedform = forms.FeedForm()
        return render(request, 'testtemplateapp/feedback.html', {'form':feedform})

def about(request):
    return render(request, 'testtemplateapp/about.html')