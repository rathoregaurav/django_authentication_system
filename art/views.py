from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework.views import APIView
from art.data import art_details
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Registration(TemplateView):

    template_name="registration.py"

    def post(self, request):
        if request.method=='POST':
            first_name = request.POST.get('firstname', None)
            last_name = request.POST.get('lastname', None)
            username = request.POST.get('email', None)
            password = request.POST.get('password', None)

            User.objects.create_user(first_name=first_name, 
                        last_name=last_name,
                        username=username,
                        password=password)
            return HttpResponseRedirect('/user/login')


class Login(TemplateView):

    template_name = "login.html"

    def post(self, request):
        if request.method=='POST':
            username = request.POST.get('email', None)
            password = request.POST.get('password', None)
            is_user_authenticate = authenticate(username=username,
                        password=password)
            if is_user_authenticate:
                login(request, is_user_authenticate)
                return HttpResponseRedirect('/user/details/')
            return render(request, 'login.html')
        if request.method=='GET':
            return HttpResponseRedirect('/user/login/')


class UserDetails(APIView):

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        print (request.user.id)
        return render(request, 'user_details.html', {"art_details":art_details})



class Logout(View):

    def get(self, request):
        logout(request)
        return render(request, "logout.html")

