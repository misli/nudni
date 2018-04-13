# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import views
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class Home(views.View):
    template_name = 'nudni/index.html'

    def get(self, request):
        lenka = models.Artist.objects.get_or_create(user=User.objects.get_or_create(username='lenka')[0])[0]
        ondrej = models.Artist.objects.get_or_create(user=User.objects.get_or_create(username='ondrej')[0])[0]
        work_list = models.Work.objects.all()
        return render(request, self.template_name, {
            'lenka': lenka,
            'ondrej': ondrej,
            'work_list': work_list,
        })
