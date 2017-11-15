# -*- coding: utf-8 -*-

"""
Django settings for nudni project.
"""

from cms_site.settings import *

# Application definition
INSTALLED_APPS = [
    'nudni',
] + INSTALLED_APPS

LOGIN_URL = '/admin/login/'
ROOT_URLCONF = 'nudni.urls'
