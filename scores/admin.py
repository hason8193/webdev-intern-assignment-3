from django.contrib import admin
from .models import Student, Subject, ForeignLanguage, ScoreStatistics


@admin.register(ForeignLanguage)
class ForeignLanguageAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['code', 'name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'is_group_a']
    list_filter = ['is_group_a']
    search_fields = ['code', 'name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sbd', 'toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'get_group_a_total']
    search_fields = ['sbd']
    list_filter = ['ma_ngoai_ngu', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Student Information', {
            'fields': ('sbd', 'ma_ngoai_ngu')
        }),
        ('Core Subjects', {
            'fields': ('toan', 'ngu_van', 'ngoai_ngu')
        }),
        ('Science Subjects (Group A)', {
            'fields': ('vat_li', 'hoa_hoc', 'sinh_hoc')
        }),
        ('Social Subjects', {
            'fields': ('lich_su', 'dia_li', 'gdcd')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_group_a_total(self, obj):
        return obj.get_group_a_total()
    get_group_a_total.short_description = 'Group A Total'


@admin.register(ScoreStatistics)
class ScoreStatisticsAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'level_excellent', 'level_good', 'level_average', 'level_below', 'total_students', 'last_updated']
    readonly_fields = ['last_updated']
    list_filter = ['last_updated']
