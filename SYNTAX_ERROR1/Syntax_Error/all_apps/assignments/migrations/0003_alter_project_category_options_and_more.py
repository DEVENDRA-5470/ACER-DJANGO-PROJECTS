# Generated by Django 5.1.1 on 2024-10-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_project_category_alter_allassignment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project_category',
            options={'verbose_name_plural': 'Project Categories'},
        ),
        migrations.AlterModelOptions(
            name='project_name',
            options={'verbose_name_plural': 'Project Name'},
        ),
    ]
