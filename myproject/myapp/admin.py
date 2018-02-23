from django.contrib import admin


# Register your models here.
from myapp.models import Person,Rent,Car

class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]

class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
	list_editable = ['stop']

admin.site.register(Person,PersonAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Rent,RentAdmin)