from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# class Term(models.Model):
#     TERM_CHOICES = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#         (6, '6'),
#         (7, '7'),
#         (8, '8'),
#         (9, '9'),
#     )
#     term_number = models.IntegerField(choices=TERM_CHOICES)
#     def __str__(self):
#         return 'term '+self.term_number.__str__()

class Student(models.Model):
    TERM_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='student_profile_images', blank=True)
    #term_id = models.ForeignKey(Term)
    term_number = models.IntegerField(choices=TERM_CHOICES,default='1')

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='teacher_profile_images', blank=True)
	
    def __str__(self):
        return self.user.username


class Subject(models.Model):
    teacher_id = models.ForeignKey(Teacher)
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(Student,through='SubjectsStudents')

    def __str__(self):
        return self.name

class SubsubjectType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subsubject(models.Model):
    subject_id = models.ForeignKey(Subject)
    teacher_id = models.ForeignKey(Teacher)
    subsubjecttype_id = models.ForeignKey(SubsubjectType)

    def __str__(self):
        return self.subject_id.name + ' (' + self.subsubjecttype_id.name + ') - ' + self.teacher_id.user.first_name + ' ' + self.teacher_id.user.last_name
        
        
class FinalGrade(models.Model):
    #look out for example if you will count average of grades!!!
    GRADE_CHOICES = (
        ('2.0', '2.0'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
        ('4.0', '4.0'),
        ('4.5', '4.5'),
        ('5.0', '5.0'),
        ('zal', 'zal'),
        ('nb', 'nb'),
        ('-','-')
    )
    student_id = models.ForeignKey(Student)
    subsubject_id = models.ForeignKey(Subsubject)
    final_value = models.CharField(max_length=3, default='-',choices=GRADE_CHOICES)
    final_date = models.DateTimeField(blank=True,null=True)
    term1_value = models.CharField(max_length=3, default='-',choices=GRADE_CHOICES)
    term1_date = models.DateTimeField(blank=True,null=True)
    term2_value = models.CharField(max_length=3, default='-',choices=GRADE_CHOICES)
    term2_date = models.DateTimeField(blank=True,null=True)
    term3_value = models.CharField(max_length=3, default='-',choices=GRADE_CHOICES)
    term3_date = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return self.subsubject_id.subject_id.name + ' ( ' + self.subsubject_id.subsubjecttype_id.name + ' ) ' + self.student_id.user.first_name + ' ' + self.student_id.user.last_name



class Subgrade(models.Model):
    GRADE_CHOICES = (
        ('2.0', '2.0'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
        ('4.0', '4.0'),
        ('4.5', '4.5'),
        ('5.0', '5.0'),
        ('zal', 'zal'),
        ('nb', 'nb'),
        ('-','-')
    )
    student_id = models.ForeignKey(Student)
    teacher_id = models.ForeignKey(Teacher)
    sub_subject_id = models.ForeignKey(Subsubject)
    value = models.CharField(max_length=3,choices=GRADE_CHOICES)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.value + ' ' + self.student_id.user.username + ' ' + self.sub_subject_id.subject_id.name + '-' + self.sub_subject_id.subsubjecttype_id.name

class SubjectsStudents(models.Model):
    TERM_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10,'10')
    )
    student_id = models.ForeignKey(Student,blank=True,null=True)
    subject_id = models.ForeignKey(Subject,blank=True,null=True)
    final_grade_id = models.OneToOneField(FinalGrade,blank=True,null=True)
    term_number = models.IntegerField(choices=TERM_CHOICES,default='1',blank=True,null=True)

    def __str__(self):
        return self.student_id.user.username + ' ' + self.subject_id.name


class SubsubjectsStudents(models.Model):
    student_id = models.ForeignKey(Student)
    sub_subject_id = models.ForeignKey(Subsubject)
    final_grade_id = models.OneToOneField(FinalGrade)

    def __str__(self):
        return self.student_id.user.username 

class Message(models.Model):
    student_id = models.ForeignKey(Student)
    teacher_id = models.ForeignKey(Teacher)
    contents = models.CharField(max_length = 400)
    is_read = models.BooleanField()
    date = models.DateTimeField(default=timezone.now)

class Survey(models.Model):
    student_id = models.ForeignKey(Student)
    teacher_id = models.ForeignKey(Teacher)
    subject_id = models.ForeignKey(Subject)
    GRADE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    teacher_grade = models.IntegerField(choices= GRADE_CHOICES)
    comments = models.CharField(max_length=1000,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.teacher_id.user.name
    
