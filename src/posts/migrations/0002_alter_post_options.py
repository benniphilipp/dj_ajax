# Generated by Django 3.2.7 on 2021-09-11 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-create',)},
        ),
    ]
