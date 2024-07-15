from django.contrib import admin

from golf.models import Events, Person, Member

# Register your models here.

admin.site.register(Events)
admin.site.register(Person)
admin.site.register(Member)


