# Generated by Django 3.0.2 on 2020-02-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmerdata', '0010_student_nctimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcontest',
            name='solve',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
