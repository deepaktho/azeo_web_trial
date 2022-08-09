from django.contrib import admin
from .models import Qviz_it_iitb
from .models import Qviz_it_noniitb
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Qviz_it_iitb)
class userdetails(ImportExportModelAdmin):
    pass

@admin.register(Qviz_it_noniitb)
class userdetails(ImportExportModelAdmin):
    pass