# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obieraki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hours', models.IntegerField()),
                ('Instructor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('ID', models.IntegerField()),
                ('ECTS', models.IntegerField()),
                ('Desription', models.TextField()),
                ('Hours', models.IntegerField()),
                ('MinStudents', models.IntegerField()),
                ('MaxStudents', models.IntegerField()),
                ('Semester', models.IntegerField()),
                ('Staff_idStaff', models.ForeignKey(to='obieraki.User_2')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.TextField()),
                ('Title', models.TextField()),
                ('User_2_idUser_2', models.ForeignKey(to='obieraki.User_2')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FieldOfStudy', models.TextField()),
                ('Year_2', models.IntegerField()),
                ('Semester', models.IntegerField()),
                ('User_2_idUser_2', models.ForeignKey(to='obieraki.User_2')),
            ],
        ),
        migrations.CreateModel(
            name='Student_has_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student_has_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_idCourse', models.ForeignKey(to='obieraki.Course')),
                ('Student_idStudent', models.ForeignKey(to='obieraki.Student')),
            ],
        ),
        migrations.RenameField(
            model_name='class_type',
            old_name='MaxStudent',
            new_name='MaxStudents',
        ),
        migrations.RenameField(
            model_name='class_type',
            old_name='MinStudent',
            new_name='MinStudents',
        ),
        migrations.AddField(
            model_name='student_has_class',
            name='Class_Class_Type_idClass',
            field=models.ForeignKey(to='obieraki.Class_Type'),
        ),
        migrations.AddField(
            model_name='student_has_class',
            name='Class_Course_idCourse',
            field=models.ForeignKey(to='obieraki.Course'),
        ),
        migrations.AddField(
            model_name='student_has_class',
            name='Student_idStudent',
            field=models.ForeignKey(to='obieraki.Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='Class_Type_idClass',
            field=models.ForeignKey(to='obieraki.Class_Type'),
        ),
        migrations.AddField(
            model_name='class',
            name='Course_idCourse',
            field=models.ForeignKey(to='obieraki.Course'),
        ),
        migrations.AddField(
            model_name='class',
            name='Staff_idStaff',
            field=models.ForeignKey(to='obieraki.Staff'),
        ),
    ]
