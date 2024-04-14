from django.contrib import admin

from . import models

# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Location)
admin.site.register(models.Language)
admin.site.register(models.Specialist)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Professional)
admin.site.register(models.UserBase)
admin.site.register(models.Product)
