from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

from .forms import Login, Profile as ProfileForm
from .models import Vacina, Banner, Profile
from datetime import datetime

import json


class TemplateView(View):
    template_name = 'home.html'

    def get(self, request):
        ban = Banner.objects.get(id=1)
        now = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

        return render(request, self.template_name, {
            'form': Login,
            'date': now,
            'banner': ban,
        })

    def post(self, request, *args, **kwargs):
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        p = Profile.objects.all().filter(cpf=cpf)
        if len(p) > 0:
            user = User.objects.get(id=p.values('user_id')[0]['user_id'])
            user = authenticate(request, username=user, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/vacina/')

            else:
                return render(request, 'access_denied.html')
                
        return render(request, 'cpf_not_found.html',{
        'profile': p,})


class CadastroView(View):
    template_name = 'cadastro.html'

    def get(self, request):

        if request.method == 'GET':
            form = ProfileForm()
            context = {'form': form}
            return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        p = request.POST

        if form.is_valid():
            if len(p.get('password')) >= 8 and p.get('password') == p.get('confirm'):

                pr = Profile.objects.all().filter(cpf=p.get('cpf'))
                us = User.objects.all().filter(username=p.get('username'))

                if len(pr) == 0 and len(us) == 0:
                    user = User.objects.create_user(
                        username=p.get('username'),
                        email=p.get('email'),
                        password=p.get('password'),
                        first_name=p.get('first_name'),
                        last_name=p.get('last_name')
                    )
                    user.profile.cpf = p.get('cpf')
                    user.profile.telefone = p.get('telefone')
                    user.profile.endereco = p.get('endereco')
                    user.profile.cidade = p.get('cidade')
                    user.save()
                    return render(request, 'thanks.html')

                else:
                    return render(request, 'user_unique.html')

            return render(request, 'password_error.html')

        context = {'form': form}
        return render(request, self.template_name, context=context)


class VacinaView(View):
    template_name = 'vacina.html'

    def get(self, request):
        now = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

        if request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            vac = Vacina.objects.all().filter(user=user)

            return render(request, self.template_name, {
                'vacina': vac,
                'date': now
            })

        else:
            return render(request, 'not_permission.html')

    def logout_view(request):
        logout(request)
        return render(request, '/')
