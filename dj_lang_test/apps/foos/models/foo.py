# -*- coding: utf-8 -*-
"""
    apps.foos.models.foo
    ~~~~~~~~~~~~~~

    foo

    :copyright: (c)  29/04/2012  by arruda.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Foo(models.Model):
    name = models.CharField(_(u"josé"),max_length=250)
    
    class Meta:
        app_label = 'foos'
        
    def __unicode__(self):
        return self.name
