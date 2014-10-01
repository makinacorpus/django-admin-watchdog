# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name=b'When')),
                ('levelname', models.CharField(verbose_name=b'Level name', max_length=20, editable=False)),
                ('shortmessage', models.CharField(verbose_name=b'Short message', max_length=256, editable=False)),
                ('message', models.TextField(verbose_name=b'Message', editable=False)),
                ('request_repr', models.TextField(verbose_name=b'Request representation', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
