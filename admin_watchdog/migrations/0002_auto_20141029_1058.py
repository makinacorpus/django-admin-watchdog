# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_watchdog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'verbose_name': 'Log entry', 'verbose_name_plural': 'Log entries'},
        ),
    ]
