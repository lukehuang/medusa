# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, unique=True, null=True, verbose_name='\u6807\u9898')),
                ('img', models.CharField(max_length=500, null=True, verbose_name='\u56fe\u7247')),
                ('link', models.CharField(max_length=500, null=True, verbose_name='\u94fe\u63a5')),
                ('source', models.CharField(max_length=500, null=True, verbose_name='\u6765\u6e90')),
                ('channel_id', models.CharField(max_length=500, null=True, verbose_name='\u9891\u9053ID')),
                ('channel_name', models.CharField(max_length=500, null=True, verbose_name='\u9891\u9053\u540d\u79f0')),
                ('desc', models.TextField(null=True, verbose_name='\u8be6\u60c5', blank=True)),
                ('datetime_publish', models.DateTimeField(null=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
    ]
