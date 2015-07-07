from django.contrib import admin

from .models import Student, Teacher, Subject, SubsubjectType, Subsubject, FinalGrade, FinalFinalGrade, Subgrade, SubjectsStudents, SubsubjectsStudents, Message, Survey

##-------------inlines

class SubsubjectInline(admin.TabularInline):
    model = Subsubject
    extra = 1


##--------------admin_models

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','term_number','field_of_study']
    list_filter = ['field_of_study','term_number']
    ordering = ['user']

class TeacherAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal data', {
            'fields': ('title','user','picture')
            }
        ),
        ('Contact', {
            'fields': ('office_hours','room','phone_number')
            }
        ),
        ('Position', {
            'fields': ('current_position','faculty','department')
        })
    )
    list_display = ['title','user','faculty','department','room','phone_number']
    list_filter = ['title']
    ordering = ['user']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','teacher_id','ECTS','exam']
    list_filter = ['teacher_id']
    inlines = [SubsubjectInline]

class SubjectsStudentsAdmin(admin.ModelAdmin):
    list_display = ['subject_id','student_id','term_number']
    list_filter = ['subject_id']

class SubsubjectsStudentsAdmin(admin.ModelAdmin):
    list_display = ['sub_subject_id','student_id']
    list_filter = ['sub_subject_id']

class FinalFinalGradeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('None', {
            'fields': (('subject_id','student_id'))
            }
        ),
        ('Grades', {
            'fields': (
                ('term1_value','term1_date'),
                ('term2_value','term2_date'),
                ('term3_value','term3_date'),
                ('final_value','final_date'),
            )
            }
        )
    )
    list_display = ['subject_id','student_id','final_value']
    list_filter = ['subject_id','student_id']

class FinalGradeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('None', {
            'fields': (('subsubject_id','student_id'))
            }
        ),
        ('Grades', {
            'fields': (
                ('term1_value','term1_date'),
                ('term2_value','term2_date'),
                ('term3_value','term3_date'),
                ('final_value','final_date'),
            )
            }
        )
    )
    list_display = ['subsubject_id','student_id','final_value']
    list_filter = ['subsubject_id','student_id']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['teacher_id','student_id','is_read','date']
    list_filter = ['student_id','teacher_id','is_read','date']

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['subject_id','teacher_id','teacher_grade','date']
    list_filter = ['teacher_id','subject_id']

class SubgradeAdmin(admin.ModelAdmin):
    list_display = ['student_id','sub_subject_id','teacher_id','value','date']
    list_filter = ['student_id','sub_subject_id','date']

##--------------models_registration

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(SubsubjectType)
#admin.site.register(Subsubject)

admin.site.register(FinalGrade,FinalGradeAdmin)
admin.site.register(FinalFinalGrade,FinalFinalGradeAdmin)
admin.site.register(Subgrade,SubgradeAdmin)
admin.site.register(SubjectsStudents,SubjectsStudentsAdmin)
admin.site.register(SubsubjectsStudents,SubsubjectsStudentsAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Survey,SurveyAdmin)


