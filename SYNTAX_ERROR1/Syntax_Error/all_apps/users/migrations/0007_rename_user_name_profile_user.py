# Generated by Django 5.1.1 on 2024-10-02 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_facebook_profile_github_profile_insta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='user',
        ),
    ]
