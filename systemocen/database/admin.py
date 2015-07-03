from django.contrib import admin

from .models import Student, Teacher, Subject, SubsubjectType, Subsubject, FinalGrade, Subgrade, SubjectsStudents, SubsubjectsStudents, Message, Survey

#--------------admin_models

class SubsubjectInLine(admin.TabularInline):
    model = Subsubject
    extra = 1

class FinalGradeChoice(admin.StackedInline):
    model = FinalGrade
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    fields = ['user']
    #inlines = [FinalGradeChoice]
    #list_display = ['user']

class FinalGradeAdmin(admin.ModelAdmin):
    pass
    #list_display = ['term1_value','term2_value']


class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None', {'fields': ['teacher_id','name']}),
        #('Subsubjects' , {'inlines': [SubsubjectInLine], 'classes': 'collapse'})
    ]
    #fields = ['teacher_id','name']
    inlines = [SubsubjectInLine]





#--------------models_registration

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(SubsubjectType)
#admin.site.register(Subsubject)
#admin.site.register(FinalGrade,FinalGradeAdmin)
admin.site.register(FinalGrade)
admin.site.register(Subgrade)
#admin.site.register(SubjectsStudents)
#admin.site.register(SubsubjectsStudents)
admin.site.register(Message)
admin.site.register(Survey)



