from django.contrib import admin

# Register your models here.
from studentdata.models import classtable,student
admin.site.register(classtable)
admin.site.register(student)