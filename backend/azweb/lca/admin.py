# Register your models here.
from django.contrib import admin
from .models import Lcauser
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Lcauser)
class userdetails(ImportExportModelAdmin):
    pass

