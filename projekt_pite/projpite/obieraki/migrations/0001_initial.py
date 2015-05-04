# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('MinStudent', models.IntegerField()),
                ('MaxStudent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Surname', models.TextField()),
                ('Mail', models.TextField(unique=True)),
                ('Login', models.TextField(unique=True)),
                ('Password_2', models.TextField()),
                ('Permission', models.IntegerField()),
            ],
        ),
    ]
