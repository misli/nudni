# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.db import models


class Artist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='artist', on_delete=models.PROTECT, unique=True)
    present = models.BooleanField('Jsem tady', default=False)
    photo = models.ImageField('Profilovka', upload_to='nudni/artist/')
    intro = models.CharField('Textík pod profilovku', max_length=400)
    color = models.CharField('Barva', default='#7a7a7a', max_length=7)

    def get_color(self):
        if self.present:
            return self.color
        else:
            return '#7a7a7a'

    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name).strip()

    def __unicode__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Umělec'
        verbose_name_plural = 'Umělci'


class Work(models.Model):
    name = models.CharField('nadpis', max_length=60)
    description = models.CharField('popis', max_length=400)
    photo = models.ImageField('Fotka', upload_to='nudni/work/')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Práce'
        verbose_name_plural = 'Práce'
