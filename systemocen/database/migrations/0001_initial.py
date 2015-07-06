# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('final_value', models.CharField(default=b'-', max_length=3, choices=[(b'2.0', b'2.0'), (b'3.0', b'3.0'), (b'3.5', b'3.5'), (b'4.0', b'4.0'), (b'4.5', b'4.5'), (b'5.0', b'5.0'), (b'zal', b'zal'), (b'nb', b'nb'), (b'-', b'-')])),
                ('final_date', models.DateTimeField(null=True, blank=True)),
                ('term1_value', models.CharField(default=b'-', max_length=3, choices=[(b'2.0', b'2.0'), (b'3.0', b'3.0'), (b'3.5', b'3.5'), (b'4.0', b'4.0'), (b'4.5', b'4.5'), (b'5.0', b'5.0'), (b'zal', b'zal'), (b'nb', b'nb'), (b'-', b'-')])),
                ('term1_date', models.DateTimeField(null=True, blank=True)),
                ('term2_value', models.CharField(default=b'-', max_length=3, choices=[(b'2.0', b'2.0'), (b'3.0', b'3.0'), (b'3.5', b'3.5'), (b'4.0', b'4.0'), (b'4.5', b'4.5'), (b'5.0', b'5.0'), (b'zal', b'zal'), (b'nb', b'nb'), (b'-', b'-')])),
                ('term2_date', models.DateTimeField(null=True, blank=True)),
                ('term3_value', models.CharField(default=b'-', max_length=3, choices=[(b'2.0', b'2.0'), (b'3.0', b'3.0'), (b'3.5', b'3.5'), (b'4.0', b'4.0'), (b'4.5', b'4.5'), (b'5.0', b'5.0'), (b'zal', b'zal'), (b'nb', b'nb'), (b'-', b'-')])),
                ('term3_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.CharField(max_length=400)),
                ('is_read', models.BooleanField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'student_profile_images', blank=True)),
                ('term_number', models.IntegerField(default=b'1', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('field_of_study', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=3, choices=[(b'2.0', b'2.0'), (b'3.0', b'3.0'), (b'3.5', b'3.5'), (b'4.0', b'4.0'), (b'4.5', b'4.5'), (b'5.0', b'5.0'), (b'zal', b'zal'), (b'nb', b'nb'), (b'-', b'-')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('student_id', models.ForeignKey(to='database.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('course_homepage', models.CharField(max_length=20, null=True, blank=True)),
                ('ECTS', models.IntegerField(default=3)),
                ('exam', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectsStudents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term_number', models.IntegerField(default=b'1', null=True, blank=True, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('final_grade_id', models.OneToOneField(null=True, blank=True, to='database.FinalGrade')),
                ('student_id', models.ForeignKey(blank=True, to='database.Student', null=True)),
                ('subject_id', models.ForeignKey(blank=True, to='database.Subject', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subsubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hours', models.IntegerField(null=True, blank=True)),
                ('subject_id', models.ForeignKey(to='database.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubsubjectsStudents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('final_grade_id', models.OneToOneField(to='database.FinalGrade')),
                ('student_id', models.ForeignKey(to='database.Student')),
                ('sub_subject_id', models.ForeignKey(to='database.Subsubject')),
            ],
        ),
        migrations.CreateModel(
            name='SubsubjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=3, choices=[(b'LEC', b'Lecture'), (b'CLA', b'Auditory classes'), (b'LAB', b'Laboratory classes'), (b'PRO', b'Project classes'), (b'SEM', b'Seminar classes'), (b'CON', b'Conversation seminars'), (b'OTH', b'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_grade', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('comments', models.CharField(max_length=1000, null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('student_id', models.ForeignKey(to='database.Student')),
                ('subject_id', models.ForeignKey(to='database.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'teacher_profile_images', blank=True)),
                ('title', models.CharField(max_length=30, null=True, blank=True)),
                ('current_position', models.CharField(max_length=40, null=True, blank=True)),
                ('faculty', models.CharField(max_length=40, null=True, blank=True)),
                ('department', models.CharField(max_length=40, null=True, blank=True)),
                ('room', models.CharField(max_length=20, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=10, null=True, blank=True)),
                ('office_hours', models.CharField(max_length=30, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='teacher_id',
            field=models.ForeignKey(to='database.Teacher'),
        ),
        migrations.AddField(
            model_name='subsubject',
            name='subsubjecttype_id',
            field=models.ForeignKey(to='database.SubsubjectType'),
        ),
        migrations.AddField(
            model_name='subsubject',
            name='teacher_id',
            field=models.ForeignKey(to='database.Teacher'),
        ),
        migrations.AddField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(to='database.Student', null=True, through='database.SubjectsStudents', blank=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher_id',
            field=models.ForeignKey(to='database.Teacher'),
        ),
        migrations.AddField(
            model_name='subgrade',
            name='sub_subject_id',
            field=models.ForeignKey(to='database.Subsubject'),
        ),
        migrations.AddField(
            model_name='subgrade',
            name='teacher_id',
            field=models.ForeignKey(to='database.Teacher'),
        ),
        migrations.AddField(
            model_name='message',
            name='student_id',
            field=models.ForeignKey(to='database.Student'),
        ),
        migrations.AddField(
            model_name='message',
            name='teacher_id',
            field=models.ForeignKey(to='database.Teacher'),
        ),
        migrations.AddField(
            model_name='finalgrade',
            name='student_id',
            field=models.ForeignKey(to='database.Student'),
        ),
        migrations.AddField(
            model_name='finalgrade',
            name='subject_id',
            field=models.ForeignKey(to='database.Subject', blank=True),
        ),
        migrations.AddField(
            model_name='finalgrade',
            name='subsubject_id',
            field=models.ForeignKey(to='database.Subsubject', blank=True),
        ),
    ]
