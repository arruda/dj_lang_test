from django.contrib import admin
from foos.models import Foo


admin.site.register(Foo, admin.ModelAdmin)