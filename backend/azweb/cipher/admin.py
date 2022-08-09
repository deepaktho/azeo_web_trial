# Register your models here.
from django.contrib import admin
from .models import Cipheruser
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Cipheruser)
class userdetails(ImportExportModelAdmin):
    pass

