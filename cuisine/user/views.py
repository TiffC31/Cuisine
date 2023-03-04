from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import login
from . import forms

def compte(request):
    return render(request, 'user/compte.html')

class SignUp(View):
    form_class = forms.SignupForm

    def get(self, request):
        return render(request, 'user/signup.html', context={'form':self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, 'user/signup.html', context={'form':form})