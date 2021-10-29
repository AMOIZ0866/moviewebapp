from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime
from movieweb.models import Movie, Signup
from movieweb.serialization import MovieSerializer, CreateUserSerializer


class Adminview(TemplateView):
    def get(self, request, **kwargs):
        movies = Movie.objects.values()
        return render(request, 'movieweb/admin/adminhome.html', {'movies': movies})

    def post(self, request):
        data = request.POST
        movies = Movie.objects.filter(Q(mname=data['name']))
        print(movies)
        return render(request, 'movieweb/admin/adminhome.html', {'movies': movies})


class AddAdminview(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'movieweb/admin/addadmin.html')

    def post(self, request):
        data = request.POST
        serializer = CreateUserSerializer(data={'username': data['username'],
                                                'password': data['password'],
                                                'email': data['email'],
                                                'last_login': datetime.now(),
                                                'type': True,
                                                'creation_date': datetime.now(),
                                                'update_date': datetime.now()})
        if serializer.is_valid():
            serializer.save()
            return render(request, 'movieweb/admin/addadmin.html', context={'alert': True})
        else:
            emessage = serializer.errors
            print(emessage.keys())
            if str(emessage.keys()) == "odict_keys(['email'])":
                error = "This Email is Already Registered"
            elif str(emessage.keys()) == "odict_keys(['username'])":
                error = "This Username is Already Registered"
            elif str(emessage.keys()) == "odict_keys(['username', 'email'])":
                error = "This Username And Email is Already Registered"
            else:
                error = "Password Error"
            return render(request,'movieweb/admin/addadmin.html', context={'error': True, 'text': error})



class AddUser(TemplateView):
    def get(self, request, **kwargs):
        user = Signup.objects.values()
        return render(request, 'movieweb/admin/viewusers.html', {'movies': user})

    def post(self, request, **kwargs):
        data = request.POST
        serializer = CreateUserSerializer(data={'username': data['username'],
                                                'password': data['password'],
                                                'email': data['email'],
                                                'last_login': datetime.now(),
                                                'creation_date': datetime.now(),
                                                'update_date': datetime.now()})
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return redirect('adduser')



class ViewUser(TemplateView):
    def get(self, request, **kwargs):
        user = Signup.objects.values()
        return render(request, 'movieweb/admin/viewusers.html', {'movies': user})

    def post(self, request):
        Signup.objects.filter(Q(username=request.POST.get("userid", ))).delete()
        user = Signup.objects.values()
        return render(request, 'movieweb/admin/viewusers.html', {'movies': user})


class ViewAdminProfile(TemplateView):
    def post(self, request):
        data = request.POST.get('username')

        userdetails = Signup.objects.filter(Q(username=data)).values().first()
        print(userdetails)
        return render(request, 'movieweb/admin/aprofile.html', context={'userdetails': userdetails})


class UpdateAdminProfile(TemplateView):
    def post(self, request):
        data = request.POST
        userdetails = Signup.objects.filter(Q(username=data['username'])).first()
        serializer = CreateUserSerializer(userdetails,data={
            'password': data['password'],
            'email': data['email'],
            'update_date': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'movieweb/admin/aprofile.html' ,context={'alert':True,'user':data['username'],'userdetails':userdetails})
        else:
            emessage = serializer.errors
            print(emessage)
            if str(emessage.keys()) == "odict_keys(['email'])":
                error = "This Email is Already Registered"
            elif str(emessage.keys()) == "odict_keys(['username'])":
                error = "This Username is Already Registered"
            else:
                error = "Password Error"
            return render(request,'movieweb/admin/aprofile.html', context={'error': True, 'text': error,'user':data['username'],'userdetails':userdetails})
