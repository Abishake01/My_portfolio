from django.contrib import admin
from .models import *

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    readonly_fields = ('uploaded_at',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'file', 'is_active')
        }),
        ('Metadata', {
            'fields': ('uploaded_at',),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Ensure only one resume is active at a time
        if obj.is_active:
            Resume.objects.filter(is_active=True).exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_url')
    search_fields = ('title', 'description')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project_url')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

@admin.register(Contact_me)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('User_name', 'link')
    search_fields = ('User_name', 'description')
    
    fieldsets = (
        (None, {
            'fields': ('User_name', 'description', 'link')
        }),
        ('Icon', {
            'fields': ('icon',)
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('is_current',)
    search_fields = ('company_name', 'job_title', 'description')
    list_editable = ('order',)

    fieldsets = (
        (None, {    
            'fields': ('company_name', 'job_title', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Display', {
            'fields': ('company_logo', 'order')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if obj.is_current:
            obj.end_date = None
        super().save_model(request, obj, form, change)