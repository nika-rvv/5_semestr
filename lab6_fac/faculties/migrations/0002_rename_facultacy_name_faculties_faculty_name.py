# Generated by Django 4.0 on 2021-12-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculties',
            old_name='facultacy_name',
            new_name='faculty_name',
        ),
    ]