# Register your models here.
from django.contrib import admin
from .models import Panel_discussionuser
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Panel_discussionuser)
class userdetails(ImportExportModelAdmin):
    pass

