# Register your models here.
from django.contrib import admin
from .models import Chemvisionuser
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Chemvisionuser)
class userdetails(ImportExportModelAdmin):
    pass

