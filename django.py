#!/usr/bin/python

import os
import re
import subprocess

def setup_install():
    print('installing pip and virtualenv so we can give django its own version of python')
    os.system('yum -y install python-pip && pip install --upgrade pip')
    os.chdir('/opt')
    os.mkdir('/opt/django')
    os.system('virtualenv django-env')
    os.system('cown -R chrisng /opt/django')
    # Using shell because python chown does not work as well

def django_install():
    print('activating virtualenv and installing django after pre-requirements have been met')
    #Must activate virtualenv shell every time you use a command for it to work from python
    os.system('source /opt/django/django-env/bin/activate && pip install django')
    # Confirms install and starts a django project
    os.chdir('/opt/django')
    os.system('source /opt/django/django-env/bin/activate ' + \
              '&& django-admin --version ' + \
              '&& django-admin startproject project1')
              
def django_start():
    print("starting django')
    os.system('chown -R chrisng /opt/django')
    os.chdir('/optdjango/project1')
    os.system('source /opt/django/django-env/bin/activate ' + \
              '&& python manage.py migrate')
    
    os.sytem('source /opt/django/django-env/bin/activate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(\'admin\',\"admin@newproject.com\',\'NTI300NTI300\')" | python manage.py shell')
    
    outputwithnewline = subprocess.check_output('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Adress: //\' -e \'s/<.*$//\' ', shell=True)
