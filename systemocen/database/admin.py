from django.contrib import admin

from .models import Student, Teacher, Subject, SubsubjectType, Subsubject, FinalGrade, Subgrade, SubjectsStudents, SubsubjectsStudents, Message, Survey

##-------------inlines
class SubjectsStudentsInline(admin.TabularInline):
    model = SubjectsStudents
    extra = 1

class StudentInline(admin.TabularInline):
    model = Student
    extra = 3

class SubsubjectInline(admin.TabularInline):
    model = Subsubject
    extra = 1

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class FinalGradeChoice(admin.StackedInline):
    model = FinalGrade
    extra = 1

##--------------admin_models

class StudentAdmin(admin.ModelAdmin):
    #fields = ['user','term_number']
    inlines = [SubjectsStudentsInline]

class SubjectAdmin(admin.ModelAdmin):
    #fieldsets = [
        #('None', {'fields': ['teacher_id','name']}),
        #('Subsubjects' , {'inlines': [SubsubjectInLine], 'classes': 'collapse'})
    #]
    inlines = [SubsubjectInline,SubjectsStudentsInline]





##--------------models_registration

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(SubsubjectType)
#admin.site.register(Subsubject)

admin.site.register(FinalGrade)
admin.site.register(Subgrade)
admin.site.register(SubjectsStudents)
#admin.site.register(SubsubjectsStudents)
admin.site.register(Message)
admin.site.register(Survey)


