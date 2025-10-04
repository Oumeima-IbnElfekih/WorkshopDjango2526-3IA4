from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header="Conference Management admin 25/26"
admin.site.site_title="Conference dashboard"
admin.site.index_title="Conference management"
admin.site.register(Conference)
admin.site.register(Submission)
