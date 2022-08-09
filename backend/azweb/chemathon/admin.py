from django.contrib import admin
from .models import Chemathon_questions,Chemathon_questions_admin
from .models import Chemathonuser
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Chemathon_questions)
@admin.register(Chemathonuser)
class userdetails(ImportExportModelAdmin):
    pass

admin.site.register(Chemathon_questions_admin)

# Register your models here.
