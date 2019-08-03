from django.contrib import admin
from .models import StudentPro
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','password']

admin.site.register(StudentPro,StudentAdmin)