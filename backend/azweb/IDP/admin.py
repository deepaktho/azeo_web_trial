from django.contrib import admin
from .models import IDPuser
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(IDPuser)
class userdetails(ImportExportModelAdmin):
    pass

