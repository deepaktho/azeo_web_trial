from django.contrib import admin
from .models import Optimiseruser
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Optimiseruser)
class userdetails(ImportExportModelAdmin):
    pass

