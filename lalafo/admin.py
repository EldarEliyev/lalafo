from django.contrib import admin
from.models.comment import Comment 
from.models.elan import Elan
from.models.location import Location
from.models.subcategory import SubCategory


# Register your models here.

admin.site.register(Comment)
admin.site.register(Elan)
admin.site.register(Location)
admin.site.register(SubCategory)