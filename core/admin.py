from django.contrib import admin

from .models import JobTitle, Service, Employee, Resources
@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'active', 'modified')
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service','icon', 'modified')
@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'active','modified')
@admin.register(Resources)
class Resources(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')




