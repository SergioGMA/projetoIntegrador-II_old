from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import Vacina, Banner, Profile
import json


class VacinaView(View):
    template_name = 'vacina.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            vac = Vacina.objects.all().filter(user=user)
            return render(request, self.template_name, {
                'vacina': vac,
            })
        else:
            return render(request, 'not_permission.html')

    def logout_view(request):
        logout(request)
        return render(request, '/')
