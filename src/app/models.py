# -*- coding: utf-8 -*-

# Copyright (c) 2017 Rohit Lodha
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.models import User

class UserID(models.Model):
    user = models.OneToOneField(User)
    organisation = models.CharField("Organisation",max_length=64, null=False, blank=False)
    lastlogin = models.DateField("Last Login",default=datetime.now,blank=True)
    def __str__(self):
        return self.user.username

class LicenseNames(models.Model):
    name = models.CharField(max_length=200)

class LicenseRequest(models.Model):
    fullname = models.CharField(max_length=70)
    shortIdentifier = models.CharField(max_length=25)
    submissionDatetime = models.DateTimeField(auto_now_add=True)
    userEmail = models.EmailField(max_length=35)
    xml = models.TextField()

    def __unicode__(self):
        return "%s" % (self.fullname)
    def __str__(self):
        return "%s" % (self.fullname)

    class Meta:
        verbose_name = "LicenseRequest"
        verbose_name_plural = "LicenseRequests"
